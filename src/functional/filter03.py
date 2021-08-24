import math

def isPrime(n):
    if n == 2:
        return True
    if n <=1 or n % 2 ==0:
        return False

    # for i in range(2, n//2 + 1):
    #     if n%i == 0:
    #         return False
    # return True
    return len(list(filter(lambda i: n%i==0, range(3, 1 + math.floor(math.sqrt(n)), 2))))==0

if __name__ == '__main__':
    p = list(filter(lambda x: isPrime(x), range(500)))
    print(p)