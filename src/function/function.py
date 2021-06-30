"""
A function is a block of organized, reusable code 
that is used to perform a single, related action.

1. Python built-in functions
print()
len()
sum()
2. User defined function
circleArea()
"""

def printName(firstName, lastName):
    print(f"First name: {firstName}, last name: {lastName}")

# call function
printName( lastName="Wang", firstName="John")

def printName(x): # overridden previously defined function
    print(f"Hello, {x}")

# printName( "Wang", "John") # previous function no long available

print(len("hello"))
# override built-in function
def len():
    print("Hello, world!")

# len("hello")

# a function can return nothing, or return one vaule, or multiple values

def getName():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    return firstName, lastName, age

# x = getName()
# print(x)
# print(type(x))
# print(f"Your first name: {x[0]}, and last name: {x[1]}.")

def circleArea(r):
    circleArea.pi = 3.1415926 # create attribute of the function, the attribute can be accessed outside by function name
    pi = 3.14 # function can have local variable which cannot be accessed outside.
    return circleArea.pi * r**2

x = circleArea(2)
print(x)
print(circleArea.pi)

# function should be single responsible
def area(x): # bad example it does the realated thing, but not single response.
    circleArea = pi * x**2
    squareArea = x*x
    return circleArea, squareArea

