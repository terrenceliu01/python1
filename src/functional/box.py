class Box:
    def __init__(self, value):
        self.value = value
    
    def getValue(self):
        return self.value

    def __eq__(self, other):
        return self.getValue()==other.getValue()
    
class Maybe(Box): # abstract class
    def __init__(self, value):
        raise NotImplementedError("Cannot create object of type Maybe: use Just(obj) or Nothing.")

class Just(Maybe):
    def __init__(self, value):
        super(Maybe, self).__init__(value) # 😄👍
    
    def __repr__(self):
        return "Just " + str(self.getValue())

class Nothing(Maybe):
    def __init__(self):
        super(Maybe, self).__init__(None)
    
    def __repr__(self):
        return "Nothing"

Nothing = Nothing()  

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
    print(x.getValue())