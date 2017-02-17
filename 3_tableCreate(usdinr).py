import psycopg2

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres", password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print "I am unable to connect to the database"
cur=db.cursor()

#creating new table
cur.execute("CREATE TABLE USDINR2016TO20170210 (Currency CHAR(15),Date DATE, \
Open REAL)")
print("Table Created....")


db.commit()
cur.close()
db.close()
