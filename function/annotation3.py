"""
document your function by annotation to avoid unexpected usage.
"""
# String slicing function that returns a string from start index to end index. 
def slice(string:'str', start: 'int', end: 'int') -> 'str': 
    return string[start:end] 
  
x = slice("abcdefghijklmnop", 2, 5)
print(x)

x = slice([1, 2, 3, 4, 5], 2, 4)
print(x)