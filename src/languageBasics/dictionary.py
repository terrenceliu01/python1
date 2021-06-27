"""
Dictionaries are Python's implementation of a data structure 
that is more generally known as an associative array. 

A dictionary consists of a collection of key-value pairs. 
It is unordered, iterable, mutable, and each paire seperated by commas, 
surrounded by {}. The key-value pairs seperated by colon.

{'key1':1, 'key2':2}
"""

# Create a dictionary
d = {}
print(type(d))
print(len(d))
d1 = {
    '1': "Monday",
    '2': "Tuesday",
    '3': "Wendsday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday",
}
print(d1)

post = dict(
    message="SS Cotopaxi", language="English"
)  # use dict() to create dict instance

# dict is iterable
for i in d1: # only iterate key
    print(i, d1[i])
print()

t1 = ((1,2),(3,4),(5,6)) # dict(iterable)
d2 = dict(t1)
print(d2)

l1 = [(1,2),(3,4),(5,6)]
d2 = dict(l1)
print(d2)

# get value by key
x = d1['4'] # use key get value
print(x)
x = d1.get('6')
print(x)
x = d1.get('8') # key does NOT exist
print(f"d1 does not contain key='8': {x}")

# dict slicing
# x = d1[1:4] # dict is unordered cannot be sliced 

# modify a dictionay ==> CRUD (Create, Retrieve, Update, Delete)
print(post)
post["userId"] = 1211      # Create a new key-value pair
print(post)
x = post['userId']         # Retrieve value by key
print(x)
post['userId'] = 'U1-1211' # Update value by given key
print(post)
del post['userId']         # Delete key-value pair from dictionary
print(post)

if "location" in post: # check if the key='location' in post dict
    print(post["location"])
else:
    print(f"no 'location' key")

# nested dictionary
d1 = {'key1':'value1'}
d2 = {'key2':'value2'}
d1['key3'] = d2
print(d1)

# dict functions (items, keys,pop)
x = d1.items()
print("79:",x)

for key, value in d1.items():
    print(key, value)

x = d1.keys()
print("85:", x)
for key in d1.keys():
    print(key)
