import sqlite3
"""
Create employee table and insert data
"""
conn = sqlite3.connect("mydb.db")

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE Employees (EmployeeID integer NOT NULL PRIMARY KEY, LastName text, FirstName text, BirthDate date, Photo text)''')
c.execute(f"INSERT INTO Employees VALUES (1, 'Davolio', 'Nancy','1968-12-18','EmpID1.pic')")
c.execute(f"INSERT INTO Employees VALUES (2, 'Fuller', 'Andrew','1996-09-19','EmpID2.pic')")
c.execute(f"INSERT INTO Employees VALUES (3, 'Leverling', 'Janet','1963-08-30','EmpID3.pic')")

# Save (commit) the changes
conn.commit()

conn.close()

print("Done.")