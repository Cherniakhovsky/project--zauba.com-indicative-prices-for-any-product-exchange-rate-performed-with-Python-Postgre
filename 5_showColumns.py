import psycopg2
import numpy as np

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres", password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print "I am unable to connect to the database"
cur=db.cursor()

cur.execute ("SELECT usdinr2016to20170210.Currency,\
             usdinr2016to20170210.Date,\
             usdinr2016to20170210.Open FROM usdinr2016to20170210")

rows=cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print row[0],row[1],row[2]
    
cur.close()
db.close()
