import psycopg2

try:
    db = psycopg2.connect(database="zauba_db",
                          user="postgres", password="12345",
                          host="127.0.0.1", port="5432")
    print("Database Connected....")
except:
    print "I am unable to connect to the database"
cur=db.cursor()

cur.execute("ALTER TABLE zauba ALTER COLUMN value_inr \
SET DATA TYPE double precision;")
cur.execute("ALTER TABLE zauba ALTER COLUMN per_unit_inr \
SET DATA TYPE numeric;")
cur.execute("ALTER TABLE zauba ALTER COLUMN per_unit_inr \
SET DATA TYPE double precision;")  

print("Table altered....")

db.commit()
cur.close()
db.close()
