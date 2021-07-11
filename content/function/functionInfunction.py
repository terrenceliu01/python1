def parent(a,b,c):
    def child(x,y):
        return x+y
    a+= child(b,c)
    return a + b + c

if __name__ == '__main__':
    x = parent (3,4,5)
    print(x)