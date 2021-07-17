import sqlite3
import uuid
"""
Create table and insert data
"""
conn = sqlite3.connect("mydb.db")

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks (ID varchar(255) NOT NULL PRIMARY KEY, date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
c.execute(f"INSERT INTO stocks VALUES ('{uuid.uuid4().hex}', '2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()

conn.close()

print("Done.")