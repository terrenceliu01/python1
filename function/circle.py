from math import pi

def circle_area(r):
    return r * r * pi

if __name__ == '__main__':
    x = circle_area(2) # call function without argument
    print(x)
    print("Done.")