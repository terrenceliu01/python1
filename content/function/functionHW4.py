def pair(srcList, target):
    """
    return a tuple if there is match, 'No match' otherwise.
    put description of the function here
    """
    for i in range(len(srcList)):
        for j in range(i+1, len(srcList)):
            if srcList[i]+srcList[j] == target :
                return i,j
    return "No match."

if __name__ == '__main__':
    numbers= (10,20,10,40,50,60,70)
    target = 60
    x = pair(numbers, target)
    print(x)