from functools import reduce

def add(x, y):
    return x + y


x = reduce(add, range(101))
print(x)