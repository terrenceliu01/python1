"""
reversing values and keys in a dictionary
"""
x = {1:11, 2:22, 3:33, 4:44, 5:55}
y = zip(x.values(), x.keys())
print(y)
z = dict(y)
print(z)
