def func1(*nums):
    print(f"funct1{nums}")
    for i in range (len(nums)):
        print(nums[i])
    print()


if __name__ == '__main__':
    a = func1(20, 40, 60)
    print()
    b = func1(80, 100)
