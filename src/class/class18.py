"""
class Inheritance
class level function
class level attritue
"""
from enum import Enum

class Mood(Enum):
    FUNKY = 1
    HAPPY = 3 
    SAD = 5

    def describe(self):
        return "John"

    @classmethod # @ is used for function decoration, function can be called by class name
    def favorite_mood(cls):
        return cls.HAPPY
    
if __name__ == '__main__':
    m = Mood(3)
    print(m)
    x = m.describe() # call instance function
    print(x)
    x = m.favorite_mood() # call classmethod
    print(x)
    x = Mood.favorite_mood()
    print(x)
    # x = Mood.describe() # describe() is an instance method, so cannot use class to call
    # print(x)