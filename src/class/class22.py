"""
__init__()
__call__()
"""

class Class1:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def __call__(self, a):
        print(a)
        print(self.x, self.y, self.z)
        return str(self.x) + str(self.y) + str(self.z)

# __call__ make the object of Class2 callable
class Class2:
    def __call__(self, a):
        return a + 10

class Class3:
    pass

if __name__ == '__main__':
    x = Class1(11, 2, 5)
    y = x(10) # use object of Class1 as a function
    print(y)

    x = Class2() 
    print(x(10)) # x is callable

    x = Class3()
    # x() # is not callable