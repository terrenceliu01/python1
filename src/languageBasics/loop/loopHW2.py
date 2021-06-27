import math 

sum = 1
for i in range(1, 11):
    print("%.2f" %(1.0/i))
    sum += 1.0/math.factorial(i)

print(sum)
print(math.e)
