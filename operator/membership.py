"""
try set, tuple
"""

l = [1,2,3,4,5]
print(3 in l)
print(10 not in l)

d1 = {1:"one",2:"two"}
print(2 in d1)
print(3 not in d1)

a="2.5"
print(type(a) in [float, int, str])

s1 = {1,2,3,4,5}
print(10 in s1)