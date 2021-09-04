from pymonad.operators.maybe import Just, Nothing
from pymonad.list import *
from pymonad.tools import curry

def positive_and_negative(x):
    return ListMonad(x, -x)

@curry(2)
def add_and_sub(x,y):
    return ListMonad(x+y, y-x)

x = ListMonad(2,3).bind(positive_and_negative).bind(add_and_sub(3))
print(x)