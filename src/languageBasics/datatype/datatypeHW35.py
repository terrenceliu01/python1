def contains(numSet, num):
    if num in numSet:
        print(f"{num} is in the set {numSet}.")
    else:
        print(f"{num} is in NOT the set {numSet}.")

nums = {1, 3, 5, 7, 9, 11}

contains(nums, 6)
contains(nums, 7)
contains(nums, 11)
contains(nums, 0)

