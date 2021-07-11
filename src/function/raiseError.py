from math import pi

def circleArea(radius):
    if type(radius) not in [float, int]:
        raise TypeError(f"the circle radius must be float or int, but '{radius}'")
    if radius < 0:
        raise ValueError(f"the circle radius cannot be negative, but radius={radius}.")
    return pi * radius**2 

if __name__ == '__main__':
    try:
        a = circleArea(2.34)
        print(a)
    except Exception as error:
        print(error)
    print("End")
