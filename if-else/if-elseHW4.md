* Write python program that ask user input an integer number, such as
"Please enter an integer number: ", if the number is enven number, 
print out "Your number is even.", otherwise print out "Your number is odd."
if the number is not an integer, print out "The number must to be an integer".

for example:

input | output
|---  |---|
4     |Your number is even.
7     |Your number is odd.
2.3   |The number must to be an integer. 
hello |The number must to be an integer. 

result = input("please enter an integer number: ")

if type(result) == int:
    if result%2==0:
        print("Your number is even")
    else:
        print("Your number is odd")
else:
    print("The number must be an integer")