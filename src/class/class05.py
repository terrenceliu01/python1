"""
define initializer __init__() use inputName as keyword argument
"""

class Robot:
    def __init__(self, inputName=None): # override default __init__()
        self.name = inputName # create instance level attribute 'name'

    def sayHello(self): # self does not count as argument
        self.energy = 1000
        if self.name:
            print(f"Hello, I'm robot {self.name}.") 
        else:
            print("Hello, I am a robot without name yet.")
    
    def add (self, a, b):
        return a + b

if __name__ == '__main__':
    r1 = Robot("Charles")
    r1.sayHello()