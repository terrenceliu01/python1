import random
rand = (random.randint(1,100))
print(rand)
count = 1
while True:
    guess = int(input("Please select a random number between 1 and 100: "))
    if guess == rand:
        print(f"You guessed it right! You made {count} times")
        
        break
    else:
        count += 1
        print("Try again!")
