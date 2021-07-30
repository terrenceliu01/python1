"""
OOP: encapsulation
protected data: _name, allow access within same module or inherit line
private data: __energy, allow access within class itself
"""

class Robot:
    def __init__(self, inputName=None, energy=1000): # override default __init__()
        self._name = inputName # create instance level attribute 'name'
        self.__energy = energy

    def __repr__(self):
        return self._name

    def sayHello(self): # self does not count as argument
        if self._name:
            print(f"Hello, I'm robot {self.name}.") 
        else:
            print("Hello, I am a robot without name yet.")
    
if __name__ == '__main__':
    r = Robot("John")
    print(r)
    # print(r.__energy) # private data not allowed outside to access it.
    print(r._name)