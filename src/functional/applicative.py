from pymonad.operators.maybe import Just, Nothing
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

@curry(3)
def addMul(x,y,z):
    return (x + y) * z

x = add *  Just(3) # Just is a Functor
print(type(x))
y = x & Just(5) # Just is a applicative
print(y)

x = addMul * Just(3) & Just(5) & Just(2)
print(x)