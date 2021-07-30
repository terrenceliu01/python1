"""
define initializer: __init__(self), create object of the class
"""

class Robot:
    def __init__(self, inputName): # override default __init__()
        self.name = inputName # create instance level attribute 'name'

    def sayHello(self): # self does not count as argument
        self.energy = 1000
        print(f"Hello, I'm robot {self.name}.") 
    
    def add (self, a, b):
        return a + b

if __name__ == '__main__':
    r1 = Robot("John")
    r1.sayHello()
    r1.name = "Marvin"
    r1.sayHello()
    