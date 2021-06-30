def trapezoidArea(upper, down, height):
    """
    return ....
    """
    return (upper+down)*height/2

if __name__ == '__main__':
    upper = float(input("Enter upper side: ")) # front tier
    down = float(input("Enter down side: "))
    height = float(input("Enter height: "))
    # validate data here
    a = trapezoidArea(upper, down, height) # middle tier
    print(a)