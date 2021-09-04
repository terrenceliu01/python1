from pymonad.operators.maybe import Just, Nothing
from pymonad.tools import curry

@curry(1)
def sayHello(person):
    return f"Hello, {person}"

print(sayHello("John"))
print(sayHello(Just("John")))
print(sayHello * Just("John")) # @curry: 1. open box before run code; 2. box result for future call; 3. tell how many arguments for the function; 4. handle Nothing
print(sayHello * Just(None)) # function's reponsibility to take care None value
print(sayHello * Nothing)

print("Done")
