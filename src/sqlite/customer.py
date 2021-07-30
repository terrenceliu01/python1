import sqlite3
"""
Create customer table and insert data
"""
conn = sqlite3.connect("mydb.db")

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE Customers (CustomerID integer NOT NULL PRIMARY KEY, CustomerName text, ContactName text, Address text, City text, PostalCode text, Country text)''')
# Insert a row of data
c.execute(f"INSERT INTO Customers VALUES (1, 'Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin','12209','Germany')")
c.execute(f"INSERT INTO Customers VALUES (2, 'Ana Trujillo','Ana Trujillo','Avada. de la Constitution 222','Mexico D.F.','05021','Mexico')")
c.execute(f"INSERT INTO Customers VALUES (3, 'Antonio Moreno','Antonio Moreno','Mataderos 2212','Berlin','05023','Mexico')")
c.execute(f"INSERT INTO Customers VALUES (4, 'Around the Horn','Thomas Hardy','120 Hanover Sq.','London','WA1 1DP','UK')")
c.execute(f"INSERT INTO Customers VALUES (5, 'Berglunds snabbkop','Christina Berglund','Berguvsvagen 8','Lulea','S-958 22','Sweden')")

c.execute('''CREATE TABLE Orders (OrderID integer NOT NULL PRIMARY KEY, CustomerID integer, EmployeeID integer, OrderDate date, ShipperID integer)''')
c.execute(f"INSERT INTO Orders VALUES (10308, 2, 7,'1996-09-18',3)")
c.execute(f"INSERT INTO Orders VALUES (10309, 37, 3,'1996-09-19',1)")
c.execute(f"INSERT INTO Orders VALUES (10310, 77, 8,'1996-09-20',2)")

# Save (commit) the changes
conn.commit()

conn.close()

print("Done.")