tuple1 = (4, 6, 2, 8, 3, 1)
print(tuple1)
tuple1 = tuple1 + (9,)
print(tuple1)
tuple1 = tuple1[:5] + (5,10,15) + tuple1[5:]
print(tuple1)
list1 = list(tuple1)
list1[4] = 30
print(list1)