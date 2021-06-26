import math
def cylinderVolume(radius, height):
    """
    Return the volume of cylinder with given radius and height
    """
    return math.pi * radius**2 * height

if __name__ == '__main__':
    r=1
    h=2
    v = format(cylinderVolume(r, h), ".3f")
    print(f"The circle area with radius={r} and height={h} is {v}")