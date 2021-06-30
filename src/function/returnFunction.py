"""
return function from a function

combine with pass function, return function, function in function
you get very good design for so called: Functional Programming vs OOP
"""

def quadratic(a, b, c):
    def f(x):
        return a * x**2 + b * x + c
    return f

if __name__ == '__main__':
    y = quadratic(1, -4, 5)
    print(type(y))
    result = y(4)
    print(result)
