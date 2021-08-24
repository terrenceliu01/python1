"""
r = map(function, sequence)
map 2 list to one
"""
from range1 import range1

def f(x, y):
    return x*y

l1 = list(range1(10))
l2 = list(range1(11,20))
l3 = list(map(f, l1, l2)) # number of variable is same as number of iterable
print(l3)