"""
Function annotation
"""
from math import pi

def circle_area(radius:'float', output:'float'=0.0) -> float:
    return pi * radius * radius

a = circle_area(2)
print(a)