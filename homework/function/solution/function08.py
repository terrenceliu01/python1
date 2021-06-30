def func1(*nums):
    for i in range (len(nums)):
        print(nums[i])


if __name__ == '__main__':
    a = func1(20, 40, 60)
    
    b = func1(80, 100)
