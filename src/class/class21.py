"""
composition vs. inheritance
"""
class Car:
    def __init__(self, model, manufacture, makeYear) -> None:
        self.model = model
        self.manufacture = manufacture
        self.makeYear = makeYear
        self.engine = self.Engine('5.1li')
    
    def __repr__(self) -> str:
        return ': '.join((self.manufacture, self.model))

    class Engine:
        def __init__(self, size) -> None:
            self.size = size
        
        def __repr__(self) -> str:
            return "Engin size: "+self.size

if __name__ == '__main__':
    car = Car("Camry","Toyota", 2009)
    print(car)
    print(car.engine)