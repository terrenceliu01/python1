def triangleArea(base,height):
    """
    Return triangle area with given base and height
    """
    return base*height/2

if __name__ == '__main__':
    b = 10
    h = 20
    a = triangleArea(b,h)  
    print(f"The trianger area with base={b} and height={h} is {a}.")