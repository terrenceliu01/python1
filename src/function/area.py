from math import pi

def circleArea(radius):
    if radius < 0:
        raise ValueError(f"the circle radius cannot be negative, but radius={radius}.")
    return pi * radius**2 

if __name__ == '__main__':
    a = circleArea(-3-5j)
    print(a)