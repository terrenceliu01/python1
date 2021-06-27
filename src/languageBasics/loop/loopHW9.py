import math

n = int(input("Enter any positive integer: "))

e = 1
for i in range(1, n+1):
    e += 1/math.factorial(i)

print("The Euler's constant is", e)