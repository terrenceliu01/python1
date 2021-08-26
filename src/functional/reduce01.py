"""
reduce: a list of items reduce to one item
r = reduce(function, sequence)
"""
from functools import reduce
from range1 import range1

def add(x, y):
    return x + y


x = reduce(add, range1(100))
print(x)

list1 = [47,11,42,13]
x = reduce(lambda x, y: x + y, list1)
print(f"the sum of list1 is {x}")
print(f"the average of list1 is {x/len(list1)}")



