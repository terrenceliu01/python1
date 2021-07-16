def isFloat(number):
    try:
        x = float(number)
        return True
    except Exception:
        return False


x = input("enter a number: ")
if(isFloat(x)):
    x = float(x)
    x = x + 4.5
    print(x)
print("End")