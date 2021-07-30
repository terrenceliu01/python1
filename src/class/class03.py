"""
Define a function inside the class
"""

class Robot:
    id = 123

    # every function defined inside class must have 'self' argument 
    # as first positional argument
    def sayHello(self): # self does not count as argument
        print(f"Hello, I'm robot {self.name}.") 
    
    def add (self, a, b):
        return a + b

if __name__ == '__main__':
    obj = Robot() # create instance of Robot
    print(type(obj))
    obj.name = "John" # runtime assign new atributte to existing class
    obj.sayHello()
    print(obj.add(4,5))
    