"""
class level attribute vs. instance level attribute
"""

class Dog:
    tricks = [] # class level attribute

    def __init__(self, name):
        self.name = name # instance level

    def addTricks(self, trick):
        self.tricks.append(trick)
    
if __name__ == '__main__':
    fido = Dog("Fido")
    fido.addTricks("roll over")
    print(f"Fido can do: {fido.tricks}")

    buddy = Dog("Buddy")
    buddy.addTricks("play dead")
    print(f"Buddy can do: {buddy.tricks}")
    print(f"Fido can do: {fido.tricks}")

    print(Dog.tricks) # use class name to refer the attribute

