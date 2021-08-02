"""
Python supports a form of multiple inheritace.
"""

class Base1:
    def __init__(self, name):
        self.name = name
    def add(self, x, y):
        return x + y
    
class Base2:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def mul(self, x, y):
        return x * y

class Subclass (Base2, Base1): # use function defined in first super class first
    pass

if __name__ == '__main__':
    s = Subclass("John")
    x = s.add(3,4)
    print(x)
    x = s.mul(5,6)
    print(x)