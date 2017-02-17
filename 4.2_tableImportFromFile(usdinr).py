import psycopg2

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres", password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print "I am unable to connect to the database"
cur=db.cursor()


#importing txt/csv file
cur.execute("COPY USDINR2016to20170210(Currency, Date, Open)  \
FROM 'D:\undinr2016-01-01to2017-10-02.txt' \
WITH DELIMITER ' ' CSV HEADER")
print "New table with columns imported"


db.commit()
cur.close()
db.close()
