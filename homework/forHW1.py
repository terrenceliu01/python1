# how many prime between 40,50
count = 0
for i in range(40,51):
    isPrime = True # every i is prime
    # check if the i is prime number
    for j in range(2,i): # not good algorithm Big O Notation: O(1), O(n), O(n^2), O(log n)
        if i%j==0: 
            isPrime = False
            break
    if isPrime:
        count = count + 1
        print(i)
print(count)