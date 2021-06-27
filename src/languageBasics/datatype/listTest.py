"""
list contains sequence of data separated by comma, surrounded by brackets.方数组
tuple is sequence of data separated by comma, surrounded by parentheses。圆数组
l = [2,3,5,7,9]
t = (2,3,5,7,9)
dir(l)
dir(t)
>>> import sys
>>> sys.getsizeof(l)
120 
>>> sys.getsizeof(t)
80
"""

# initial empty list
l = []
print(type(l))

l = list()
print(len(l))

# list slicing
myList = [6, 7, 8, 9, 10]
l1 = myList[1]
l1 = myList[0:2]
l1 = myList[2:10]
l1= myList[:10]
l1 = myList[0:4:2] #increament by 2
print(l1)

# list - Add, Delete and sort
myList = [6, 3, 1, 19, 10]
print(myList)
myList.append(11)
myList.insert(3, 11)
myList.remove(11) # where 11 is the value of the element
v = myList.pop(2) # where 2 is index
print(v)

# mixed datatype in a list
student1=[1234, 'Amy', "Liu", 13]
print(student1)
student1[3]=11

# nested list
l = [[1,2],[3,4,5],[6,7,8,9]]
print(l)
print(len(l))
print(len(l[0]))


# Create list
l = [1,2,3,4,5]
print(l)

for n in l: # list is iterable
    print(n)

l=list(range(10))
print(l)

f = lambda x: x%2==0
l = list(filter(f, range(20)))
print(l)

squares = []
for i in range(1, 101):
    squares.append(i**2)
print(squares)

l = [range(4), range(10, 15)]
l1 = [y for x in l for y in x] # flatten two list
print(l1)

# list Comprehension vs. For loop
l1 = [i for i in range(20) if i%2==1]
print(l1)

l1 = [i*4 for i in range(10)]
print(l1)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

l1 = [letter for letter in "Hello World!"] # string is iterable
print(l1)

l1 = [i*3+j**2 for i in range(5) for j in range(3)]
print(l1)

movies = [("Citizen Kane", 1941),("Spirited Away",2001),("It's a Wonderful Life",1946),("Gattaca",1997),("No Country for Old Men",2007),("Rear Window",1954),("The Lord of the Rings",2001),("Groundhog Day",1993),("Close Encounters of the Third Kind",1977),("The Royal Tenenbaums",2001),("The Aviator",2004),("Raiders of the Lost Ark",1981)]
before2000 = [(title, year) for (title, year) in movies if year<2000]
print("47:",before2000)

A = (1,3,5,7)
B = (2,4,6,8)
l1 = [(a,b) for a in A for b in B]
print(l1)

l = [False]*6 # create a default boolean list
print(l)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(f"The number of apples is {fruits.count('apple')}.")
print(f"The number of tangerine is {fruits.count('tangerine')}.")
print(f"The index of banana is {fruits.index('banana')}.")
print(f"The index of next banana is {fruits.index('banana', 4)}.")
fruits.reverse() # reverse function does NOT return anything
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())
print(fruits)

# modify list
l[4] = "hello"
print(l)
l1 = l[3:7]
print(l1)
l1 = fruits[::-1]
print(fruits)
print(l1)
l.append(20)
print(l)
l.insert(0, "First")
print(l)
l.append(l1) # list in list
print(l)
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

faces = ('A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("SPADES", "CLUBS", "DIAMONDS", "HEARTS")
cards = [(face, suit) for suit in suits for face in faces]
print(cards)
print(len(cards))

a = [1,2,3]
b = [4,5,6]
c = list(zip(a, b))
print(c)

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
numbers = [2, 1, 3, 4, 7]
print(*numbers, *fruits)
