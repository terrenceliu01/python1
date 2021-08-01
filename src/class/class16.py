"""
class inheritance, 
"""

class SuperClass:
    def __init__(self, a):
        self.instanceData = a
    
    def __repr__(self):
        return str(self.instanceData)

    def __len__(self):
        return 5

    def superFunc(self):
        print("superFunc() is running...")
    
class Subclass(SuperClass):
    def __repr__(self): # function collision 后来者居上
        return "Subclass"

    def subFunc(self):
        print("subFunc() is running...")

if __name__ == '__main__':
    sub = Subclass([1,2,3])
    print(sub)
    sub.superFunc()
    sub.subFunc()
    print(len(sub))
    print(isinstance(sub, SuperClass)) # is relationship
    sup = SuperClass(1)
    print(isinstance(sup, Subclass))