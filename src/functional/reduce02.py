"""find maximum or minimum"""
from functools import reduce

list1 = [47, 11, 42, 102, 13]
max = lambda a, b: a if (a > b) else b
x = reduce(max, list1)
print("max =", x)

x = reduce(lambda a, b: a>b and a or b, list1)
print(x)

min = lambda a, b: a if (a < b) else b
x = reduce(min, list1)
print("min =", x)

x = reduce(lambda a, b: a<b and a or b, list1)
print(x)

x = reduce(lambda x, y: x+y, list1)
print(x)

x = reduce(lambda x, y: x+y, list1, 10) # initial value =0 by default
print(x)