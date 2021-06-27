# Python Data Type
* Primitive Data Type: int, char, float, double...
* Non-Primitive Data Type: 
  - linear data structure
  >The arrangement of data in a sequential manner is known as a linear data structure. The data structures used for this purpose are Arrays, Linked list, Stacks, and Queues. In these data structures, one element is connected to only one another element in a linear form.

  - non-linear data structure
  >When one element is connected to the 'n' number of elements known as a non-linear data structure. The best example is trees and graphs. In this case, the elements are arranged in a random manner.
* Static data structure:
  >It is a type of data structure where the size is allocated at the compile time. Therefore, the maximum size is fixed.
* Dynamic data structure:
  >It is a type of data structure where the size is allocated at the run time. Therefore, the maximum size is flexible.

## Homeworks
* datatypeHW1.md; use dict find month name
* datatypeHW2.md; use dict find square of a integer
* datatypeHW3.md; sum all integers in a list
* datatypeHW4.md; multiply all integers in a list
* datetypeHW5.md; find max number in a list
* datatypeHW6.md; sort a list which contains tuple item by second tuple item.
* datatypeHW7.md; remove duplicate number in the list
* 
## Basic Data Type

![Python Data Type](../../images/DataType.png)
* bool
    - True (1)
    - False (0)
* Number
    - int
    - float
    - complex
* String
    - str
* Tuple
    - tuple
* List
    - list
* Set
  prove True=1, False=0
    - set
* Dictionary
    - dic
## Major Operations
* Searching
* Sorting
* Insertion
* Updation
* Deletion

## Define variable data type  
python, does not like other language, determine the data type at data assignment time.
```
>>> a = 5
>>> type(a)
>>> a = 3.4
>>> type(a)
>>> a = 4 + 5j
>>> type(a)
>>> a = (1,2,3)
>>> type(a)
>>> a = [4,6,5]
>>> type(a)
>>> a = {1,2,3}
>>> type(a)
>>> a = {"k1":"value1","k2":"value2"}
>>> type(a)
```
## get individual item from tuple, list and dict
```
a = (1,2,3,4,5)
a[1]

a = {"k1":"value1","k2":"value2"}
a["k1"]
a.get("k1")
```
## Different data type in Tuple or list
```
a = (1,2,'hello',4,5)
```

## change values in tuple, list, set and dict
```
>>> a = [1,2,3,4]
>>> a.append(5)
>>> a = {1,2,3}
>>> a.add(5)
>>> a.add(3)
```
## Operator on tuple, list, set, ...
* + on tuple
```
a = (1,2,3)
b = (4,5,6)
b + a
```
* + on list
```
a = [1,2,3]
b = [4,5,6]
a + b
a * 2
```