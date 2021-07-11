def f(a, b):
    return a + b

def ff(f, x, y):
    return f(x,y)

if __name__ == '__main__':
    x = ff(f, 3, 4)
    print(x)