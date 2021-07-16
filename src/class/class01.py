"""
🔥a Python class is for defining a particular type of object abstracted from real world.
Python classes define what methods can be used to change the state of an object.

1. class name
2. data
3. function

💡the data and function also indicate as object attribute of the class.

class <className>:
    pass

🔥👇class is the fundation of OOP, and OOP has following 4 features
1. abstraction   实体模拟 (abstract object from real world to Python class)
2. inheritance   共性继承 (inherit one class from other to increase code reusability)
3. polymorphism  异类同功 (回答相同的问题，由于不同的类型，which inherite from same class or interface，而给出不同答案)
4. encapsulation 自我保护 (avoid private state being changed from outside class)
"""

class Robot: # All class inherits from 'object' class
    pass

if __name__ == '__main__':
    robot1 = Robot() # create an instance(object) of Robot
    print(robot1)
    print(type(robot1))
    print(robot1.__dict__)
    robot2 = Robot()
    robot3 = robot1
    print(robot1==robot2)
    print(robot1==robot3)

    robot1.name = "Marvin"
    robot1.buildYear = 2013

    print(robot1.name)
    print(robot3.buildYear)

    robot3.name = "John"
    print(robot1.name)

    robot2.name = "David" # instance level attribute, only belong to the object
    print(robot1.name)

    Robot.brand = 'GE' # class level attribute shared by all objects
    print(robot1.brand)
    print(robot2.brand)

