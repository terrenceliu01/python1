from random import randint

def roll(*dice): 
    print(f"Number of dices is {len(dice)}.")
    return sum(randint(1, die) for die in dice)

x= roll(6,6,6)
print(f"Total number is {x}")
if 6*3/2 < x:
    print("大")
else:
    print("小")

x= roll(6,6)
print(x)
if 6 < x:
    print("大")
else:
    print("小")