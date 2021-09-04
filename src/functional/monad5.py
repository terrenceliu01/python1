from pymonad.reader import Compose

def add1(x):
    return x + 1

def mul3(x):
    return x*3

newFunc = Compose(add1).then(mul3).then(str)
print(newFunc(9))
x = "hello " + newFunc(4)
print(x)