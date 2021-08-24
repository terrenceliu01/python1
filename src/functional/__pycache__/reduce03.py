"""
using operator module
"""

from functools import reduce
from operator import * # import operator

list1 = [7,11,2,12,3]
print(f"The product of list element is: {reduce(mul, list1)}")
