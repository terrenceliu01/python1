from math import pi

def circleArea(radius):
    if radius < 0:
        raise ValueError(f"the circle radius cannot be negative, but radius={radius}.")
    return pi * radius**2 

if __name__ == '__main__':
    try:
        a = circleArea(-3)
        print(a)
    except Exception as error:
        print(error)
    print("End")