from functools import reduce

list1 = [47, 11, 42, 102, 13]

x = reduce(lambda a, b: a if a>b else b, list1)
print(x)

x = reduce(lambda a, b: a>b and a or b, list1)
print(x)

