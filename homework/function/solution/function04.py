import math
def circle_area(radius):
    """
    Return the area of circle with given radius
    """
    return math.pi * radius**2

if __name__ == '__main__':
    r = 1
    a = format(circle_area(r), ".3f")
    print(f"The circle area with radius={r} is {a}")