"""
Define function inside another function
"""
def parent(a, b, c):
    def child(x, y):
        return x / y
    
    a += child(b, c)
    return a + b + c

if __name__ == '__main__':
    x = parent(3, 4, 5)
    print(x)
    # x = parent.child(4,7) # so called encapsulation, protect child to called outside
    # OOP: Object Oriented Programming has 4 basic features.
    # 1. abstraction   抽象性
    # 2. inheritance   继承性
    # 3. polymorphism  回答相同的问题，由于不同的类型，which inherite from same class or interface，而给出不同答案
    # 4. encapsulation 保护性