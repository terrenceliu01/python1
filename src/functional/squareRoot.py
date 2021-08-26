"""
math in real world need for function chain
"""
count = 1 # global variable
def next(n, x):
    return (x + n/x)/2

def recursion(e, x): # e: epsilon
    n = 2
    a = next(n, x)
    b = next(n, a)
    global count
    count += 1
    if abs(a-b) <= e: # 1. termination condition
        return b
    return recursion(e, b) # 2. call itself; 3. adjust recursion variable toward termination

if __name__ == '__main__':
    n = 2 # calculate square root of 2
    f = lambda x: next(n,x) # make two arguments to one
    a0 = 1
    l1 = [round(x, 5) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))), f(f(f(f(a0)))))]
    print(l1)

    x = recursion(0.000001, 1)
    print(x)
    print(count)