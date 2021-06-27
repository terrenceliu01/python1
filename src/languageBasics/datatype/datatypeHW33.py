x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
#use isdisjoint(). Return True if the set has no elements in common with other. 
print("There is no common element in x and y: ",x.isdisjoint(y))
#use difference(). Return a new set with elements in the set that are not in the others.
print("The elements in x but not in y are: ",x.difference(y))
#new set with elements from both x and y
print("Merger x and y is: ",x | y)