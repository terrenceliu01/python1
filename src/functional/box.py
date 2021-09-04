class Box:
    def __init__(self, value):
        self.value = value
    
    def getValue(self): # open box
        return self.value

    def __eq__(self, other):
        return self.getValue()==other.getValue()
    
class Maybe(Box): # abstract class
    def __init__(self, value):
        raise NotImplementedError("Cannot create object of type Maybe: use Just(obj) or Nothing.")

class Just(Maybe): # Just is a functor
    def __init__(self, value):
        super(Maybe, self).__init__(value) # 😄👍
    
    def __repr__(self):
        return "Just " + str(self.getValue())

    def fmap(self, func):
        return func(self)

    def __mul__(self, func): # define '*' operator
        return self.fmap(func)

    def bind(self, func):
        return func(self)

    def __rshift__(self, function):
        return self.bind(function)

class Nothing_(Maybe):
    def __init__(self):
        super(Maybe, self).__init__(None)
    
    def __repr__(self):
        return "Nothing"

    def fmap(self, func):
        return self

    def __mul__(self, func): # define '*' operator
        return self.fmap(func)

Nothing = Nothing_()  

def add3(num):
    return Just(num.getValue()+3)

def mul10(num):
    return Just(num.getValue()*10)

if __name__ == '__main__':
    x = Box(2)
    print(type(x))
    print(x.getValue()) # open box, unwrapper
    # x = Maybe(2) # cannot use Maybe to create an instance
    x = Just(2)
    print(x)
    x = Nothing
    print(x)
    print(isinstance(x, Box))
    print(x==Nothing)
    print(x is Nothing)
    print(x.getValue())

    y = Just(2).fmap(add3).fmap(mul10)
    print(y)

    y = Just(3) * add3
    print(y) 

    y = Nothing * add3 * mul10
    print(y)

    x = Just(2) >> add3 >> mul10
    print(x)