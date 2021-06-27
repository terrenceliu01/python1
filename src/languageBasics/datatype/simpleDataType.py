"""
Simple data type
"""
# number
n = 5
print(type(n))
print("07:", n)
x = str(n)
print("08:", type(x), x)

n = 4.5
print(type(n))
print(n)
x = str(n)
print("15:", type(x), x)

# string
h = "hello"
print("18:", type(h))
print(h)

# cannot use + to add int and str type
# print(n+h) #print(str(n)+h) # need convert int to str first

n = " world"  # override or reassign value to variable n
print(h + n)

# boolean
x = True
y = False

print(type(x))
print(type(y))
"""
phthon
>>> True
True
>>> true
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
"""

a, b = 4, 7
print(a == b)
print(a != b)
print(a > b)
print(a < b)

print("51:", bool(2))
print("52:", bool(-2.3))
print("53:", bool(0))  # convert to bool is False

print(bool("hello"))
print(bool(""))

x = str(True)
print(type(x), x)

x = input("Please enter a number: ")
x = int(x)

x = int(True)
print(type(x), x)
x = int(False)
print(type(x), x)

x = float(True)
print(type(x), x)
x = float(False)
print(type(x), x)

x = 5 + True
print(x)

x = 10 * False
print(x)