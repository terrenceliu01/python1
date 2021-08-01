"""
__new__(cls): object constructor, 
__init__(self): initializer the object
"""

class A(object): # all class inherits from object class, __init__, __new__, __repr__
    def __new__(cls):# constructor
        print("A.__new__() is called.")
        return super(A, cls).__new__(cls)
    

class C():
    def __new__(cls, name): # constructor
        print("C.__new__() is called.")
        return super(C, cls).__new__(cls)

    def __repr__(self):# return a string to represent this instance
        return self.name + self.ssn

    def __init__(self, inputName): #
        print("C.__init() is called")
        self.name = inputName
        self.ssn = "111-11-1111"
        # return 5

if __name__ == '__main__':
    a = A()
    print(type(a))
    print(a)

    c = C("John") # c is intance of C class
    print(type(c))
    print(c)