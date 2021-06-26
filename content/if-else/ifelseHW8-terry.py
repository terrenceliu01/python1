guess = int(input("Guess a number between 0-9: "))
import random
num = random.randint(0,9)
if guess == num:
    print("You are correct!")
else:
    print("Try again!")

