from pymonad.operators.maybe import Just, Nothing

def add3(x):
    if x is Nothing:
        return Nothing
    return Just(x + 3)

def sub5(x):
    if x is Nothing:
        return Nothing
    return Just(x - 5)

def mul7(x):
    if x is Nothing:
        return Nothing
    return Just(x * 7)

def div9(x):
    if x is Nothing:
        return Nothing
    return Just(x/9)

if __name__ == '__main__':
    f = lambda x: Just(x) >> add3 >> sub5 >> add3 >> mul7 >> div9
    x = f(20)
    print(x)
    print(x.value)

    x = f(Nothing)
    print(x)