from pymonad.operators.maybe import Just, Nothing
from pymonad.list import *

list0 = ListMonad(1,2,3,4)
print(type(list0))
print(type(list0[2]))

def neg(x):
    return -x

def add3(x):
    return x + 3

x = list0.map(neg)
print(x)

x = list0.then(neg).then(add3) # different function chain
print(x)