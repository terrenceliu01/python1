from pymonad.operators.maybe import Just, Nothing
from pymonad.tools import curry


def add3(x):
    return Just(x + 3)


def mul4(x):
    return Just(x * 4)


def half(x):
    return Just(x/2)

def func(x): # define goal (functinal programming)
    return Just(x) >> add3 >> mul4 >> half


# x = mul4 * (add3 * Just(2))  # functor
# print(x)

x = Just(2) >> add3 >> mul4 >> half # override bitwise operator >> right-shift, so-called monad
print(x)

x = Just(2).bind(add3).bind(mul4).bind(half)
print(x)


x = func(2)
print(x)