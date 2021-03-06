<h1> Python Language Basic </h1>

[Interesting Icons](myIcons.md)

- [My First python program](#my-first-python-program)
- [print(with variable)](#printwith-variable)
- [comment (single line, multiple line)](#comment-single-line-multiple-line)
- [Variable Naming](#variable-naming)
- [Data Type](#data-type)
- [Operator](#operator)
- [Execution Control](#execution-control)
- [Loop](#loop)
- [function](#function)
- [Unit test](#unit-test)
- [Logging](#logging)
- [SQLite](#sqlite)
  - [CRUD (Create, Retreive, Update, Delete)](#crud-create-retreive-update-delete)
  - [join](#join)
  - [left join](#left-join)
  - [right join](#right-join)
  - [full join](#full-join)
  - [self join](#self-join)
  - [Union](#union)
  - [GROUP BY](#group-by)
  - [INSERT INTO SELECT](#insert-into-select)
- [class](#class)
  - [class basic](#class-basic)
  - [dunder function in class](#dunder-function-in-class)
  - [class tricks](#class-tricks)
  - [attribute scope](#attribute-scope)
  - [class inheritance](#class-inheritance)
- [Blackjack Card Game](#blackjack-card-game)
- [Yahtzee Dice Game](#yahtzee-dice-game)
- [Documentation](#documentation)
  - [Document for developer](#document-for-developer)
- [Integration Test](#integration-test)
  - [Document for user](#document-for-user)
- [Deployment](#deployment)
- [File Access](#file-access)
- [Plot](#plot)
- [Lambda Expression](#lambda-expression)
- [map function](#map-function)
- [filter function](#filter-function)
- [reduce() function](#reduce-function)
- [Clean Code](#clean-code)
  - [Design Principles SOLID](#design-principles-solid)
- [Functional programing](#functional-programing)
  - [calculate square root](#calculate-square-root)
  - [Functor](#functor)
  - [Applicative](#applicative)
  - [Monad](#monad)


## My First python program
[hello.py](../src/hello.py)

## print(with variable)
[print.py](../src/print.py)
```py
print(f"The circle area with radius={r} is {a:.2f}")
```

## comment (single line, multiple line)
[comment.py](../src/languageBasics/comment.py)
* single line comment
* multiple line comment

## Variable Naming
1. variable name cannot start with number
2. variable can be combination of letters and numbers _, a~z, A~Z, 0~9, no other special characters
3. don't use reserved keywords as variable name
![](images/pythonKeywords.png)
[Python Keywords](https://realpython.com/python-keywords/#:~:text=%20Python%20Keywords%20and%20Their%20Usage%20%201,are%20used%20for%20control%20flow%3A%20if%2C...%20More%20)
4. Avoid using existing function name as your variable name.
otherwise, your python builtins functions no longer works the way you expected.
![](images/chineseMedicine.jpg)
![](images/memory.gif)

![](images/LanguageBasics.svg)

## Data Type
* [Numbers](../src/languageBasics/number.py)
    - int
    - float
    - complex
* [String](../src/languageBasics/string.py)
    - iterale
    - slicing
    - +, *, <, > operators
    - built in functions (isdigit, isalnum, title, ...)
* [Tuple](../src/languageBasics/tuple.py)
    - iterable
    - immutable
    - slicing
    - +, * operator
* [List](../src/languageBasics/list.py)
    - iterable
    - mutable
    - slicing
    - +, * operator
    - built in functions (append, insert, remove, pop, ...)
* [Set](../src/languageBasics/set.py)
    - iterable
    - mutable
    - built in functions(add, )

* [Dict](../src/languageBasics/dictionary.py)
    - iterable: only iterate key


## Operator 
* [operator](../src/languageBasics/operator.py)
* [arithmatic](../src/languageBasics/operator/arithmatic.py)
* [assignment](../src/languageBasics/operator/assignment.py)
* [comparison](../src/languageBasics/operator/comparison.py)
* [identity](../src/languageBasics/operator/identity.py)
* [logical](../src/languageBasics/operator/logical.py)
* [membership](../src/languageBasics/operator/membership.py)
* [others](../src/languageBasics/operator/others.py)
* [ternary](../src/languageBasics/operator/ternary.py)
* [bitwise](../src/languageBasics/operator/bitwise.py)

## Execution Control
* **if-elif-else** statement Syntax
```py
if <condition>:
    # if code block here
elif <condition>:
    # elif code block here
else:
    #else code block here
# code continue ...
```
* Mermaid Diagram for if-else statement
```mermaid
graph TB
A((start))
B{if <condition>:}
C[if code block]
D[else code block]
E[end]


A-->B
B--True-->C-->E
B--False-->D-->E

A1((start))
B1{if <condition>:}
B2{elif <condition>:}
C1[if code block]
D1[elif code block]
E1[end]
F1[else code block]

A1-->B1
B1--True-->C1-->E1
B1--False-->B2--True-->D1-->E1
B2--False-->F1-->E1


classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:#DE9E1F,stroke-width:2px;
classDef start fill:green,stroke:#DE9E1F,stroke-width:2px;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px;
class A,A1 start
class B,B1,B2 html
class E,E1 end1
```
* [if-else1.py](../src/../content/if-else/if-else1.py)
## Loop
* [simple for loop](../src/languageBasics/loop/for1.py)
* [simple while loop](../src/languageBasics/loop/while.py)
  - a while loop 
```mermaid
graph TB
B([Python Program])
C[Python function]
D[Python class]
E[data == Attribute]
F[function]

B --write--> C
B --write--> D
D -->E & F

classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:#DE9E1F,stroke-width:2px;
classDef start fill:green,stroke:#DE9E1F,stroke-width:2px;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px;
class START start
class C,D html
class END end1
```

## function
    - def, Python reserved keyword
    - function name, anything you want, but need follow the naming rules
    - (), must have open/close parenthesis pair, no matter it has arguments or not
    - arguments, positional or keyword arguments separated by comma ,
    - :, must end with colon
    - the function body must indent
    - ????????????function can be overridden
    - ????return more than one value
    - ????single response
    - call a function by function name and (), and arguments if there is any

-  Other function uses
    - can have functions in functions 
      - [Function In Function](../src/function/functionInFunction.py)
    - passing function to function means that we can create many different functions first with the same amount of values taken in, then use their property to calculate specific values for the target function 
      - [pass function as argument](../src/function/passFunction2function.py)
    - return function can be used to return a function such as the quadratic function, and can be used to calculate specific values when plugged into these equations 
      - [return Function from function](../src/function/returnFunction.py)
$$
\underbrace {def}_{keyword} \underbrace {circle \_area}_{function \space name} \left(\underbrace {a, b,c ...}_{positional\; args} * \underbrace {e=None, f=200}_{keyword\;args}\right) \underbrace {:}_{eol}
$$

* [Function Basics](../src/function/function.py)
??????never override built-in functions and your previous defined function if you still need them.
* [Function in function](../src/function/functionInFunction.py)
* [Return function from function](../src/function/returnFunction.py)
* [pass function as argument](../src/function/passFunction2function.py)
  

???What is OOP? What are differences between Functional Programming and OOP
??????4 Features of OOP
  1. Abstraction:class is a abstraction of object in real world to python program object type.??????????????????
  2. Inheritance: a class can inherit from multiple other class to increase code reusability.??????????????????
  3. Polymorphism:same function behavior differently by different object type.??????????????????
  4. Encapsulation???avoid data or function being called outside the class unintentionally???????????????)

* [raiseError.py](../src/function/raiseError.py)
* [assertCheck.py](../src/function/assertCheck.py)

the differenct between raise and assert:
1. assert: I swear this must bt true, help developer
2. raise: try to catch run-time error. sometime developer will use raise to control execution flow.

[a sample of using try-except to control flow](../src/function/checkFloat.py)

```mermaid
graph TB
A[Try]
B[No error block]
C[Raise Error]
D[Continue Block]
END[end]
F[except block]
G[Wait for <br>service request]

A-->B-->C-->F--blows up-->END
B-->D-->G

classDef html fill:#12DBE2,stroke:#12DBE2,stroke-width:4px,color:#E21912;
classDef js fill:yellow,stroke:#DE9E1F,stroke-width:2px;
classDef start fill:#299F30,stroke:#0B7111,stroke-width:2px;
classDef if fill:#EFAE58,stroke:#EFAE58,color:#5899EF;
classDef end1 fill:#F46661,stroke:#F12D26,stroke-width:2px;

class START start
class B,C,D html
class G js
class IF if
class END end1
```

```mermaid
graph LR
A([Software Project])
D[User Interface]
E[Business Logic]
F[Database]
G["No SQL(MongoDB)"]
H["SQLite RelastionalDB"]
I[Window Based]
J[Web Based]
K[ReactJS]
L[Angular]
M[DJango]
UNIT(Unit Test<br>TDD)
LOG(Logging)
DOC(Documentation)
INTG(Integration Test)
DEPLOY(Deployment)


A --> D & E & F & UNIT & LOG & DOC & INTG & DEPLOY
D-->I & J
F-->G & H
J-->K & L & M

classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:#98CAF5,stroke:#98CAF5,stroke-width:2px;

class D,E,F html
class UNIT,LOG js
```

## Unit test
* configure unit test:
    Right-Click ??? Command Palette... ??? Configure Tests ??? unittest ??? test ??? test_*.py
    
## Logging
* write execution record to file. (database) used to do application analysis.
* category to different level: Debug, Info, Warning, Error, Fatal

[logging](../src/log/logging1.py)

## SQLite
???What is DBA?

??????A Database Administrator (**DBA**) is individual or person responsible for controlling, maintenance, coordinating, and operation of database management system. ... Their role also varies from configuration, database design, migration, security, troubleshooting, backup, and data recovery.

[SQL Interview Website](https://www.interviewbit.com/sql-interview-questions/)

???What is Database?

>??????A database is an organized collection of data, stored and retrieved digitally from a remote or local computer system. Databases can be vast and complex, and such databases are developed using fixed design and modeling approaches.

???What is DBMS?

>??????DBMS stands for Database Management System. DBMS is a system software responsible for the creation, retrieval, updation and management of the database. It ensures that our data is consistent, organized and is easily accessible by serving as an interface between the database and its end users or application softwares.

???What is RDBMS? How is it different from DBMS?

>??????RDBMS stands for Relational Database Management System. The key difference here, compared to DBMS, is that RDBMS stores data in the form of a collection of tables and relations can be defined between the common fields of these tables. Most modern database management systems like MySQL, Microsoft SQL Server, Oracle, IBM DB2 and Amazon Redshift are based on RDBMS.

???What is SQL?

>??????SQL stands for Structured Query Language. It is the standard language for relational database management systems. It is especially useful in handling organized data comprised of entities (variables) and relations between different entities of the data.

???What are Tables and Fields?

>??????A table is an organized collection of data stored in the form of rows and columns. Columns can be categorized as vertical and rows as horizontal. The columns in a table are called fields while the rows can be referred to as records.

???What are Constraints in SQL?

>??????Constraints are used to specify the rules concerning data in the table. It can be applied for single or multiple fields in an SQL table during creation of table or after creationg using the ALTER TABLE command. The constraints are:

Constraints| Description
|---       |---         | 
NOT NULL   |Restricts NULL value from being inserted into a column.
CHECK      |Verifies that all values in a field satisfy a condition.
DEFAULT    | Automatically assigns a default value if no value has been specified for the field.
UNIQUE     |Ensures unique values to be inserted into the field.
INDEX      |Indexes a field providing faster retrieval of records.
PRIMARY KEY|Uniquely identifies each record in a table.
FOREIGN KEY|Ensures referential integrity for a record in another table.

???What is Primary Key?

>??????The PRIMARY KEY constraint uniquely identifies each row in a table. It must contain UNIQUE values and has an implicit NOT NULL constraint.

A table in SQL is strictly restricted to have one and only one primary key, which is comprised of single or multiple fields (columns).

* [Create, PRIMARY KEY](../src/sqlite/sqlite0.py)

???What is UNIQUE constraint?

??????A UNIQUE constraint ensures that all values in a column are different. This provides uniqueness for the column(s) and helps identify each row uniquely. Unlike primary key, there can be multiple unique constraints defined per table. The code syntax for UNIQUE is quite similar to that of PRIMARY KEY and can be used interchangeably.

```SQL
CREATE TABLE Students ( 	 /* Create table with a single field as unique */
    ID INT NOT NULL UNIQUE
    Name VARCHAR(255)
);

CREATE TABLE Students ( 	 /* Create table with multiple fields as unique */
    ID INT NOT NULL
    LastName VARCHAR(255)
    FirstName VARCHAR(255) NOT NULL
    CONSTRAINT PK_Student
    UNIQUE (ID, FirstName)
);

ALTER TABLE Students 	 /* Set a column as unique */
ADD UNIQUE (ID);

ALTER TABLE Students 	 /* Set multiple columns as unique */
ADD CONSTRAINT PK_Student 	 /* Naming a unique constraint */
UNIQUE (ID, FirstName);
```

???What is a Foreign Key?

??????A FOREIGN KEY comprises of single or collection of fields in a table that essentially refer to the PRIMARY KEY in another table. Foreign key constraint ensures referential integrity in the relation between two tables.
The table with the foreign key constraint is labelled as the child table, and the table containing the candidate key is labelled as the referenced or parent table.

```sql
CREATE TABLE Supplier (
  SupplierNumber INTEGER NOT NULL,
  Name           VARCHAR(20) NOT NULL,
  Address        VARCHAR(50) NOT NULL,
  CONSTRAINT supplier_pk PRIMARY KEY(SupplierNumber),
  CONSTRAINT number_value CHECK(SupplierNumber > 0)
)

CREATE TABLE Invoice (
  InvoiceNumber  INTEGER NOT NULL, 
  Text           VARCHAR(4096),
  SupplierNumber INTEGER NOT NULL,
  CONSTRAINT invoice_pk PRIMARY KEY(InvoiceNumber),
  CONSTRAINT inumber_value CHECK (InvoiceNumber > 0),
  CONSTRAINT supplier_fk
    FOREIGN KEY(SupplierNumber) REFERENCES Supplier(SupplierNumber)
    ON UPDATE CASCADE ON DELETE RESTRICT
)
```
![](images/foreignKey.svg)

???What is an Index? Explain its different types

??????A database index is a data structure that provides quick lookup of data in a column or columns of a table. It enhances the speed of operations accessing data from a database table at the cost of additional writes and memory to maintain the index data structure.

* Unique and Non-Unique Index:
>Unique indexes are indexes that help maintain data integrity by ensuring that no two rows of data in a table have identical key values. Once a unique index has been defined for a table, uniqueness is enforced whenever keys are added or changed within the index.

??????????* Clustered and Non-Clustered Index:
>Clustered indexes are indexes whose order of the rows in the database correspond to the order of the rows in the index. This is why only one clustered index can exist in a given table, whereas, multiple non-clustered indexes can exist in the table.

???What is the difference between Clustered and Non-clustered index?

>?????????? the differences can be broken down into three small factors 
1. Clustered index modifies the way records are stored in a database based on the indexed column. Non-clustered index creates a separate entity within the table which references the original table.
2. Clustered index is used for easy and speedy retrieval of data from the database, whereas, fetching records from the non-clustered index is relatively slower.
3. In SQL, a table can have a single clustered index whereas it can have multiple non-clustered indexes.

???What is a Query?

??????A query is a request for data or information from a database table or combination of tables. 
1. select query or 
2. an action query.

???What is a Subquery? What are its types?

??????A subquery is a query within another query, also known as nested query or inner query .
1. A **correlated subquery** cannot be considered as an independent query, but it can refer the column in a table listed in the FROM of the main query.
2. A non-correlated subquery can be considered as an independent query and the output of subquery is substituted in the main query.

???What are some common clauses used with SELECT query in SQL?

??????Some common SQL clauses used in conjuction with a SELECT query are as follows:
1. WHERE clause in SQL is used to filter records that are necessary, based on specific conditions.
2. ORDER BY clause in SQL is used to sort the records based on some field(s) in ascending (ASC) or descending order (DESC).
3. GROUP BY clause in SQL is used to group records with identical data and can be used in conjuction with some aggregation functions to produce summarized results from the database.
4. HAVING clause in SQL is used to filter records in combination with the GROUP BY clause. It is different from WHERE, since WHERE clause cannot filter aggregated records

???What is Cursor? How to use a Cursor?

??????A database cursor is a control structure that allows for traversal of records in a database.
```sql
DECLARE @name VARCHAR(50) 	 /* Declare All Required Variables */

DECLARE db_cursor CURSOR FOR 	 /* Declare Cursor Name*/
SELECT name
FROM myDB.students
WHERE parent_name IN ('Sara', 'Ansh')

OPEN db_cursor 	 /* Open cursor and Fetch data into @name */ 
FETCH next
FROM db_cursor
INTO @name

CLOSE db_cursor 	 /* Close the cursor and deallocate the resources */
DEALLOCATE db_cursor
```

???What are Entities and Relationships?

```mermaid
classDiagram
class Invoice{
  ID NOT NULL PRIMARY KEY
  CustomerID:INT
}

class Customer{

}



```
??????**Entity:** An entity can be a real-world object, either tangible or intangible, that can be easily identifiable. For example, in a college database, students, professors, workers, departments, and projects can be referred to as entities. Each entity has some associated properties that provide it an identity.
??????**Relationship:** Relations or links between entities that have something to do with each other. For example - The employees table in a company's database can be associated with the salary table in the same database.
* one-to-many & Many-to-one
* Many-to-Many
* Self Referencing Relationship: This is used when a table needs to define a relationship with itself.
  
![](images/many-to-many.png)

![](images/Intersection-Entity.png)

???What is a View?

??????A view in SQL is a virtual table based on the result-set of an SQL statement. A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

???What is Normalization?

??????????Normalization represents the way of organizing structured data in the database efficiently. It includes creation of tables, establishing relationships between them, and defining rules for those relationships. Inconsistency and redundancy can be kept in check based on these rules, hence, adding flexibility to the database.

??????????????????????????????

???What is Denormalization?

??????Denormalization is the inverse process of normalization, where the normalized schema is converted into a schema which has redundant information. The performance is improved by using redundancy and keeping the redundant data consistent. The reason for performing denormalization is the overheads produced in query processor by an over-normalized structure.

???What are the TRUNCATE, DELETE and DROP statements?
??????

???What is PL/SQL Oracle Stored Procedure?

??????A stored procedure is a set of Structured Query Language (SQL) statements with an assigned name, which are stored in a relational database management system (RDBMS) as a group, so it can be reused and shared by multiple programs.

```sql
CREATE OR REPLACE procedure_name(arg1 data_type, ...) AS
BEGIN
  ....
END procedure_name;

CREATE OR REPLACE procedure_name(arg1 data_type, ...) AS
BEGIN
  ....
END procedure_name;
```

AWS: Amazon Web Service
Firebase:

???What is function

??????
```sql
CREATE OR REPLACE
FUNCTION calculate_score
( cat IN VARCHAR2
, score IN NUMBER
, weight IN NUMBER
) RETURN NUMBER AS
BEGIN
  RETURN NULL;
END calculate_score;
```
???What is Trigger?

??????A trigger is a special type of stored procedure that automatically runs when an event occurs in the database server. 

```sql
-- SQL Server Syntax  
-- Trigger on an INSERT, UPDATE, or DELETE statement to a table or view (DML Trigger)  
  
CREATE [ OR ALTER ] TRIGGER [ schema_name . ]trigger_name   
ON { table | view }   
[ WITH <dml_trigger_option> [ ,...n ] ]  
{ FOR | AFTER | INSTEAD OF }   
{ [ INSERT ] [ , ] [ UPDATE ] [ , ] [ DELETE ] }   
[ WITH APPEND ]  
[ NOT FOR REPLICATION ]   
AS { sql_statement  [ ; ] [ ,...n ] | EXTERNAL NAME <method specifier [ ; ] > }  
  
<dml_trigger_option> ::=  
    [ ENCRYPTION ]  
    [ EXECUTE AS Clause ]  
  
<method_specifier> ::=  
    assembly_name.class_name.method_name  
  
```

### CRUD (Create, Retreive, Update, Delete)
* Create (Insert into)
  [sqlite insert](../src/sqlite/sqlite1.py)

* Retreive (Select * from ... where ...)
  [sqlite select](../src/sqlite/sqlite2.py)

* Update 
  [sqlite update](../src/sqlite/sqlite4.py)

* Delete
  [sqlite delete](../src/sqlite/sqlite5.py)

### join
???What is a Join? List its different types
??????

![](images/join.png)

 **(inner) join**: Retrieves records that have matching values in both tables involved in the join. This is the widely used join for queries.

![](images/img_innerjoin.gif)

```sql
SELECT *
FROM Table_A
JOIN Table_B;

SELECT *
FROM Table_A
INNER JOIN Table_B;

SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```
[Customers and Orders](../src/sqlite/customer.py)

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

```output
10308	Ana Trujillo
```

### left join
 **LEFT (OUTER) JOIN:** Retrieves all the records/rows from the left and the matched records/rows from the right table.

```sql
SELECT *
FROM Table_A A
LEFT JOIN Table_B B
ON A.col = B.col;
```
![](images/img_leftjoin.gif)

[Customers and Orders](../src/sqlite/customer.py)

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
```
CustomerName | OrderID
|---|---|
Alfreds Futterkiste|NULL	
Ana Trujillo	   |10308
Antonio Moreno	   |NULL

### right join
 **RIGHT (OUTER) JOIN:** Retrieves all the records/rows from the right and the matched records/rows from the left table.

```sql
SELECT *
FROM Table_A A
RIGHT JOIN Table_B B
ON A.col = B.col;
```

![](images/img_rightjoin.gif)

[Customers and Orders](../src/sqlite/employee.py)

```sql
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
```
???????RIGHT and FULL OUTER JOINs are not currently supported
```output
Execution finished with errors.
Result: RIGHT and FULL OUTER JOINs are not currently supported
At line 1:
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees
```

### full join
 **FULL (OUTER) JOIN:** Retrieves all the records where there is a match in either the left or right table.

![](images/img_fulljoin.gif)

### self join
* **Self Join** Syntax
  
```sql
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```
[Customers and Orders](../src/sqlite/customer.py)

????The following SQL statement matches customers that are from the same city:

```sql
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
```

CustomerName1 | CustomerName2 | City
|---          |---            |---       |
Alfreds Futterkiste	|Antonio Moreno	     |Berlin
Antonio Moreno	    |Alfreds Futterkiste |Berlin

### Union

```sql
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```
[supplier.py](../src/sqlite/supplier.py)

```sql
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
```
```output
Ann Arbor
Berlin
London
Mexico D.F.
New Orleans
```

### GROUP BY

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```
[Customers and Orders](../src/sqlite/customer.py)

```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
```

```output
2	Mexico
1	UK
1	Sweden
1	Germany
```

### INSERT INTO SELECT

* Copy all columns from one table to another table:

```sql
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
```

* Copy only some columns from one table into another table:

```sql
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```
* [create table for one-to-many relation](../src/sqlite/sqlite6.py)
* [insert one-to-many data](../src/sqlite/sqlite7.py)
* [retrieve one-to-many data](../src/sqlite/sqlite8.py)
* Homework: create sample code for many-to-many, such as customer-to-provider
* [Create books sqlite database table](../src/sqlite/sqlite9.py)
* [insert data for books](../src/sqlite/sqlite10.py)
* [CRUD for books](../src/sqlite/sqlitebookdb.py)


## class
???What is class?
>??????Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state, or do some special thing.

```mermaid
graph LR
A([Data type])
B[Python Builtins]
C[User Defined]

A--> B & C
```

### class basic
* [Syntax to create simplest class](../src/class/class01.py)
* [define a function outside of a class](../src/class/class02.py)
* [Define a function inside the class](../src/class/class03.py)
* [define initializer: __init__(self)](../src/class/class04.py)
* [use inputName as keyword argument, make default __init__ work](../src/class/class05.py)
* [protected and private data _, __](../src/class/class07.py)
* [getter, setter, property](../src/class/class08.py)
* 
### dunder function in class
* [__repr__, __str__,](../src/class/class06.py)
* [__new__, __init__](../src/class/class09.py)
  - if override both __init__ and __new__, you need same arguments.
  - don't override __new__, onless you have to.
  - __new__ is constructor which return the instance of class
  - __init__ is initializer which only initialize the instance reutn None.
  - python always call __new__ first and then __init__.
* [__iter__, __next__](../src/class/class15.py)
    - [range1.py](../src/class/range1.py)
* [__call__, make object callable](../src/class/class22.py)
* [__gt__, __lt__,__eq__,__add__](../src/class/class24.py)
  

### class tricks
* [override __new__ can return different class intance](../src/class/class10.py)
* [avoid duplicated code block](../src/class/class13.py)
* [__call__, make object callable](../src/class/class22.py)
* [@classmethod vs. @staticmethod](../src/class/class23.py)

### attribute scope
* [class level attribute](../src/class/class11.py)
* [instance level attribute](../src/class/class12.py)

### class inheritance
* [class inheritance](../src/class/class16.py)
    - subclass inherits all features from superclass(constructor, repr, func, attributes)
    - could override all features from superclass
    - subclass can define its own function and attributes
* [Enum, Enum is callable.](../src/class/class17.py)
* [classmethod vs. instance method](../src/class/class18.py)

* composition vs. Inheritance
```mermaid
classDiagram

class Employee{
  name:string
  employeeId:int
}

class Manager{
  employee:Employee
  assignWork()
}

Employee<|--Manager:inheritance is
```
```py
assign Manager.employee = None
```

## Blackjack Card Game
* [design document](blackjack.md)
* [if without else, dynamic winner() function](../src/blackjack.py)
* [Unit test for blackjack](../test/test_blackjack.py)

## Yahtzee Dice Game
[Yahtzee Dice Game](https://www.dicegamedepot.com/yahtzee-rules/)


## Documentation
### Document for developer
???Why do I need document my code?
??????

## Integration Test
???
??????

### Document for user

## Deployment

## File Access
* [write string to file, ./, ../](../src/files/file01.py)
* [read and append to file](../src/files/file02.py)
* [with open, automatically close file](../src/files/file03.py)
* [build student list from json file](../src/files/file04.py)
* [dump json to file](../src/files/file05.py)
* [load json string do dict](../src/files/file06.py)
* [read csv](../src/files/file07.py)
* [plot csv](../src/files/file08.py)
* [write csv from dict](../src/files/file09.py)


## Plot

## Lambda Expression
??? What is lambda expression
??????A Lambda function in Python programming is a anonymous function, or a function having no name.

* Syntax:
```py
lambda <variable list separated by comma>: expression
```

1. short intline function
2. one time used
3. can assign a function name

## map function
???What is map() function?
??????the map() function is processing iterable without looping.

![](images/map.png)

1. two iterable not necessary to be the same length, the smaller will be used
2. apply function to each element in the iterable
3. the varaible order is same as iterable order
4. out iterable has the same size of the smaller iterable

* [r = map(function, sequence)](../src/functional/map01.py)
* [convert temperature for-loop vs map](../src/functional/map02.py)
* [temperature converter with lambda expression](../src/functional/map03.py)


## filter function
???What is filter function?
??????filter function return an iterable yielding those items of iterable for which function(item) is true. If function is None, return the item that are true.

1. return iterable with size <= original iterable
2. function is a boolean function return True or False

* Syntax:
```py
filter(function or None, iterable) --> filter object
```
* [filter(function, squence)](../src/functional/filter01.py)
* [filt by temperature](../src/functional/filter02.py)
* [for vs filter](../src/functional/filter03.py)


## reduce() function
???What is reduce() function?
?????? The reduce(func, seq) function is used to apply a particular function passed in its arguments to all of the list elements.

* [a list of items reduce to one item](../src/functional/reduce01.py)

## Clean Code
[How to write good code](../../doc/Clean-Code.pdf)

### Design Principles SOLID

[SOLIDS website](https://stackify.com/solid-design-principles/)

1. Single Responsibility principle
  >A class should have one, and only one, reason to change. You need to change your class as soon as one of its responsibilities changes. it makes your software easier to implement and prevents unexpected side-effects of future changes.
2. Open/Close Pricinple
  >Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
3. Liskov Substitution Principle
   >Let ??(x) be a property provable about objects x of type T. Then ??(y) should be true for objects y of type S where S is a subtype of T.
4. Interface Segregation Principle
  >Clients should not be forced to depend upon interfaces that they do not use.
5. Dependency Inversion
  >High-level modules, which provide complex logic, should be easily reusable and unaffected by changes in low-level modules, which provide utility features. 
  
?????????requirements change over time. least code change on requirement changes.???

## Functional programing
??? What is functional programming?
?????? functional programming is a programming paradigm where programs are constructed by applying and composing functions. 
* [pass and return function](../src/functional/myTimer1.py)
* [function decorator](../src/functional/myTimer2.py)
### calculate square root
$$ a_{i+1} = \frac {(a_i + \frac n {a_i})} 2 $$
$$ a_1 = f(a_0) $$
$$ a_2 = f(f(a_0)) $$

### Functor
??? What is a functor?
??????Functor is a 'wrappered box value' can be applied by a function. a container class implements fmap() function.

![Functor, applicative, monad](images/monad.png)

* [normal function call vs. fuction operator](../src/functional/functor.py)
??? Why use wrapper box on number?
?????? to solve very common program issue
1. Null pointer exception
2. function call failure

* [Sample for null pointer and function call failure](../src/functional/whyWrapperBox.py) 

```mermaid
graph TB

A(Input/output <br>value)
B[Good value<br>Just]
C[Bad value<br>Nothing]

A-->B & C

D(function)
E[Successful<br>Right]
F[Failed<br>Left]

D-->E & F

classDef start fill:green,stroke:#DE9E1F,stroke-width:2px,color:white;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px,color:white;

class B,E start
class C,F end1
```

```mermaid
classDiagram

class Box{
  value:any_object
}
class Functor{
  fmap(function)
}

Box<|--Functor
```
 * [Understand functor, applicative and monad](../src/functional/box.py)
 * [Understand @curry function decorator](../src/functional/monad1.py)
  1. tell how many arguments
  2. open box before run the function
  3. box the result for future call
  4. handle Nothing before function call


### Applicative
??? What is applicative?
?????? you apply a wrapperd function to a warapped value using apply. if the Wrapper class implement amap() function, then the wrapper class is a applicative.
??????apply function to wrapper boxed values one after another, all the values are applicatives.

### Monad
```mermaid
classDiagram

class Box{
  value:any
}
class Functor{
  fmap(function)
  map(function)
}
class Applicative{
  amap(functorValue)
}
class Monad{
  bind(function)
  __rshift__(function)
}
class Just{
  value:any
}

Box<|--Functor
Functor<|--Just
Functor<|--Applicative
Applicative<|--Just
Monad<|--Just

```

ReactiveX
![](images/ReactiveAction.gif)

Machine Learning
Docker
Kubernate
AWS
DevOps