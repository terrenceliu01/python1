"""
function defined outside of the class
"""

def f1(self, x, y):
    return min(x, x+y)

class A:
    f = f1
    def g(self):
        return "Hello"

class B:
    f = f1
    def add(self, x, y):
        return x + y

if __name__ == '__main__':
    x = A()
    y = x.f(4, -3)
    print(y)

    x=B()
    y = x.f(4, -3)
    print(y)

    y = f1(None,4,-3)
    print(y)