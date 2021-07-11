def quadratic(a, b, c):
    def f(x):
        return a*x**2 + b*x + c
    return f

if __name__ == '__main__':
    y = quadratic(1, -4, 5)
    result = y(4)
    print(result)