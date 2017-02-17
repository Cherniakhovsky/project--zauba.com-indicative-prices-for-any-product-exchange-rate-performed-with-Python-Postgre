import psycopg2
import os
print open(os.getcwd()+'TNT.txt')
directory=os.getcwd()

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres", password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print ("I am unable to connect to the database")
cur=db.cursor()

#put appropriate directory below
#importing txt file, preliminary to delete ',' and
#change ',' to '.' 
#from integers of this .txt file with the help of Excel

cur.execute("COPY zauba(Date, HS_Code, Description,\
Origin_Country, Port_of_Discharge,Unit,\
Quantity,Value_INR, Per_Unit_INR)\
FROM 'D:\TNT.txt' WITH DELIMITER '	' CSV HEADER")
print ("New table with columns imported")

db.commit()
cur.close()
db.close()
