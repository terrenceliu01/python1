def addList(l1, l2):
    ziplist = zip(l1,l2)
    return [x + y for (x, y) in ziplist]

if __name__ == '__main__':
    l1 = [1,2,3]
    l2 = [4,5,6]
    l = addList(l1,l2)
    print(l)