"""
__new__(cls): object constructor, 
__init__(self): initializer the object
"""

class A(object): # all class inherits from object class, __init__, __new__, __repr__
    def __new__(cls):
        print("A.__new__() is called.")
        return super(A, cls).__new__(cls)
    

class C():
    def __new__(cls, name): 
        print("C.__new__() is called.", name)
        cls.name = name
        return super(C, cls).__new__(cls)

    def __repr__(self):
        return self.name

    def __init__(self, inputName):
        print("C.__init() is called")
        # self.name = inputName

if __name__ == '__main__':
    a = A()
    print(type(a))
    print(a)

    c = C("John")
    print(type(c))
    print(c)