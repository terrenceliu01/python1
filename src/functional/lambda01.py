print(lambda x: x*x) # no name inline function

def myfunction(x): # have name
    return x*x

print(myfunction)

# def f(x):
#     return 3*pow(x,2) - 5*x + 4

f = lambda x: 3*pow(x,2) - 5*x + 4 # assign function name to lambda 
list1 = [f(x) for x in [1,4,6,7,33]]
print(list1)
y = f(3)
print(y)

t3 = tuple(map(lambda x, y: x+y, [1,2,3,4],[5,6,7,8])) # get rid of loop, iterable in, iterable out
print(t3)

from math import pi
t3 = list(map(lambda r: r*r*pi, [3,1,7,2] ))
print(t3)