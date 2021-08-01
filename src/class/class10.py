"""
a trick about override __new__()
make one class create another class instance possible
"""

class Sample(object):
    def __repr__(self):
        return "SAMPLE"
    
    def add(self, x, y):
        return x + y

class A:
    def __new__(cls): # by default return instance of this class
        return Sample() # call Sample class __new__()

if __name__ == '__main__':
    a = A()
    print(type(a))  
    print(a)      
    