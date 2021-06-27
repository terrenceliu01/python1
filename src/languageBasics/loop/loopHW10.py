n = int(input("Enter an integer: "))

f = 0
for i in range(n+1):
    f += i

print(f"The sum from 1 to {n} is {f}.")