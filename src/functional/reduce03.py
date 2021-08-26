from functools import reduce
import operator

list1 = [7, 11, 2, 12, 3]
print(f"The product of list element is: {reduce(operator.mul, list1)}\n")

