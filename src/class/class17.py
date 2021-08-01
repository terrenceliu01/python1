"""
Python module: enum
enumeration: the act of naming things seperatly, one by one:
"""

from enum import Enum

class Color(Enum):
    RED = 6 # RED is a contant
    GREEN = 1 # class level attribute
    BLUE = 3

if __name__ == '__main__':
    x = Color.GREEN
    print(x)
    print(x.name)
    print(x.value)
    print(type(x))
    print(x.__dict__)
    print(type(x) is Color)
    print(isinstance(x, Color))
