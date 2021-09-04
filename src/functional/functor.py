"""
Functor is a 'wrappered box value' can be applied by a function
"""
from pymonad.operators.maybe import Just

def add3(number):
    return number + 3

x = add3(2) # normal way to call function
print(x)

x = add3 * Just(2) # Just is a functor
print(x)

x = Just(2).map(add3)
print(x)