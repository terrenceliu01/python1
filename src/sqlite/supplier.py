import sqlite3
"""
Create supplier table and insert data
"""
conn = sqlite3.connect("mydb.db")

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE Suppliers (SupplierID integer NOT NULL PRIMARY KEY, SupplierName text, ContactName text, Address text, City text, PostalCode text, Country text)''')
c.execute(f"INSERT INTO Suppliers VALUES (1, 'Exotic Liquid', 'Charlotte Copper','49 Gilbert St.','London','EC1 4SD', 'UK')")
c.execute(f"INSERT INTO Suppliers VALUES (2, 'New Orleans Cajun Delights', 'Shelley Burke','P.O. Box 78934','New Orleans','70117','USA')")
c.execute(f"INSERT INTO Suppliers VALUES (3, 'Grandma Kelly Homestead', 'Regina Murphy','707 Oxford Rd.','Ann Arbor', '48104', 'USA')")

# Save (commit) the changes
conn.commit()

conn.close()

print("Done.")