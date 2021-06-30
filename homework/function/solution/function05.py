def findPair(numbers, target):
    """py
    input tuple/list
    return tuple
    Find a pair of numbers in a given tuple/list that add up to the designated target number
    """
    for i in range(len(numbers)):
        for j in range (i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                return i,j
        

if __name__ == '__main__':
    numbers= (10,20,10,40,50,60,70)
    target=60
    a = findPair(numbers, target)
    print(a)

