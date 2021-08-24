"""
filter(function, squence)
return iterable which <= original one
"""

def isEven(n):
    return n % 2 == 0

l1 = list(range(1,11))

l2 = tuple(filter(isEven, l1))
print(l2)

l2 = tuple(filter(lambda x: x%2==0, l1))
print(l2)

l2 = tuple(filter(None, (1, 3, 0, 5, 2, 0, 9))) # Non-Trivial is True
print(l2)

l2 = tuple(filter(None, ['', None, "Hello", ' ', "world"]))
print(l2)