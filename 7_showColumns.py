# -*- coding: cp1251 -*-
import psycopg2

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres", password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print "I am unable to connect to the database"
cur=db.cursor()

##SQL запит:
##SELECT zauba.date,zauba.quantity, zauba.value_inr, 
##zauba.value_inr/zauba.quantity/usdinr2016to20170210.open AS USDtn,
##usdinr2016to20170210.date,usdinr2016to20170210.open 
##FROM public.zauba LEFT OUTER JOIN public.usdinr2016to20170210
##ON zauba.date=usdinr2016to20170210.date
##ORDER BY zauba.date DESC

cur.execute ("SELECT zauba.date,zauba.quantity,zauba.value_inr,\
             zauba.value_inr/zauba.quantity/usdinr2016to20170210.open AS USDtn,\
             usdinr2016to20170210.date,usdinr2016to20170210.open\
             FROM zauba LEFT OUTER JOIN usdinr2016to20170210 \
             ON zauba.date=usdinr2016to20170210.date \
             ORDER BY zauba.date DESC;")

rows=cur.fetchall()

print "\nShow me the databases:\n"
print "   Date:   |", "   USD/tn   "
print "--------------------------"
for row in rows:
    print row[0],'|',row[3]
    
cur.close()
db.close()
