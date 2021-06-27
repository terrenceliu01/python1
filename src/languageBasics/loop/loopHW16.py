def isPrime(x):
    for i in range(2, (x//2+1)):
        if(x % i == 0):
            return False
    else: # use for-else syntax
        return x>1

if __name__ == '__main__':
    for i in range(40, 51):
        if isPrime(i):
            print(i, end=' ')