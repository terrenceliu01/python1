"""
Write a Python program to get a list, sorted in increasing 
order by the last element in each tuple from a given 
list of non-empty tuples.
"""
def second(n): # define sort function
    return n[-1]

def sort_list_second(tuples):
    return sorted(tuples, key=second)

l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sort_list_second(l))