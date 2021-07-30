"""
__repr__
__str__
__len__
"""

class A:
    pass
    def __init__(self, myList):
        self.mylist = myList
        self.name = "John Wang"

    def __repr__(self): # override existing dunder function
        return "John" + "(12345)"

    def __str__(self): # similar with Java toString()
        return "Terry"

    def __len__(self):
        return 8

if __name__ == '__main__':
    a = A([1,2,3,5,7,12,23])
    print(a)
    print(repr(a))
    print(str(a))
    print(len(a))