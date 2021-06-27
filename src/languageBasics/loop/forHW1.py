x = 40
y = 51

for i in range(x, y):
    isPrime = True
    for j in range(2, i): 
        if i % j == 0: # if there is any number with reminder = 0, it is not prime
            isPrime = False
            break
    if isPrime:
        print(i)