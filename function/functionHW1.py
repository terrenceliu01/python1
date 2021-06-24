def triangleArea(base,height):
    """
    return triangle area for give base and height.
    """
    return base*height/2

if __name__ == '__main__': # below is the test code to make sure my code works
    b = 10
    h = 20
    area = triangleArea(b,h)
    print(f"The trianger area with base={b} and height={h} is {area}.")

