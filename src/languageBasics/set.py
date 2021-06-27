""" 
A Set is an unordered collection Python objects that is iterable, 
mutable and separated by comma, has no duplicate elements, surrounded by {}.集合 

set1 = {1,2,3,4,5}
"""

# Create set
set1 = set()
set2 = set()

odds = set(range(1,11,2))
print(odds)

evens = set(range(0,11,2))
print(evens)

print(len(evens))

# set is iterable
for el in evens:
    print(el, end=' ')
print()

# set licing
# x = odds[0]
# odds[1]=12

# modify set(add, discard, remove, pop)
set1 = set(range(1, 6))
set2 = set(range(3, 8))
print(set1)
print(set2)
set1.add(11)
print(set1)
set1.add(2) # no duplicate item allowed in set.
print(set1)
set1.discard(3)
print(set1)
x=set1.pop()
print(x)
print(set1)
# set3 = set()
# set3.pop()
set1.remove(11)
print(set1)

# Operator on set:
# & intersection
# | union
# > 
# <
# ==


# relationship between sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)

"""
A set is an unordered collection of Python objects that is iterable,
mutable and has no duplicate elements, surrounded by {}.集合

set1 = {1,2,3,4}
"""

# Creating set
set1 = set()
set2 = set()

for i in range(1, 6):
    set1.add(i)

for i in range(3, 8):
    set2.add(i)

print(set1)
print(set2)

set3 = set("hello") # use set function pass iterable to create new set
print(set3)

evens = set(range(0,10,2))
print(evens)
odds = set(range(1,10,2))
print(odds)
set3 = set([6,7,12,3,5,89])
print(set3)

# set is iterable
for item in set1:
    print(item, end=', ')
print()
print(len(set1))
print(sum(set1))

# set slicing
# x = set1[3] # set is unordered, cannot be sliced

# modify set (add, clear, pop, remove, discarrd)
set1.add(15)
print(set1)
set1.add(2) # no duplicate item allowed in set.
print(set1)
set1.discard(15)
print(set1)
set1.discard(20) # do nothing if element not exist
print(set1)
# set1.remove(20)
set1.remove(3)
print(set1)
x = set1.pop()
print(x)
print(set1)


# Operator on set:
# & intersection
# | union
# > 
# <
# ==
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1 & set2
print(set1)
print(set2)
print(set3)
set3 = set1 | set2
print(set3)
set1 = {1,2,3,4,5,6}
set2 = {2,3,4}
print(set1>set2)
print(set1<set2)
print(set1==set2)

# functions for  (union, update,difference,intersection,isdisjoint)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)