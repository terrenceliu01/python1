import random

"""
rolling two dice and display the result of the two dice
"""
def main():
    min = 1
    max = 6
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are....")
        print(random.randint(min, max))
        print(random.randint(min, max))

        roll_again = input("Roll the dices again?")

if __name__ == '__main__':
    main()