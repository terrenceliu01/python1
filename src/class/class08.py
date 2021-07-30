"""
access none public attributes: getter, setter, and property
"""
class Robot:
    def __init__(self, inputName=None, energy=1000, user=("John", "password")): # override default __init__()
        self._name = inputName # create instance level attribute 'name'
        self.__energy = energy
        self.__user = user

    def __repr__(self):
        return self._name

    def sayHello(self): # self does not count as argument
        if self._name:
            print(f"Hello, I'm robot {self.name}.") 
        else:
            print("Hello, I am a robot without name yet.")

    def getName(self): #getter
        return self._name
    
    def setName(self, newName): # setter
        if self.__user[0]=="Wang":
            self._name = newName

    def delName(me):
        print("delName() is called!!!")
        del me._name

    name = property(getName, setName, delName)

if __name__ == '__main__':
    r = Robot("John",user=("Wang",1234))
    r.setName("Terry")
    print(r)
    print(r.name)
    r.name = "David"
    del r.name

    print(r)
