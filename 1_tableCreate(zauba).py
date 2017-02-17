import psycopg2

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres",password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print ("I am unable to connect to the database")
cur=db.cursor()

#creating new table
cur.execute("CREATE TABLE zauba (Date DATE, HS_Code INTEGER,	\
Description CHAR(200),Origin_Country CHAR(20), Port_of_Discharge CHAR(20), \
Unit CHAR(10), Quantity double precision, Value_INR MONEY, Per_Unit_INR MONEY)")
print("Table Created....")


db.commit()
cur.close()
db.close()
