"""
function decorator
"""

import time

def my_timer(original): # pass function to function
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original(*args, **kwargs) # call original function
        t2 = time.time() - t1
        print(f"{original.__name__} ran in {t2:.1f} seconds.")
        return result
    return wrapper # return function

@my_timer
def display_info(name, age):
    time.sleep(2)
    print(f"display_info()... ran with arguments: ({name}, {age})")

@my_timer
def anotherFunc(a, b, /, c, d, *, e=1, f=2):
    time.sleep(1)
    print(f"{a}, {b}, {c}, {d}, {e}, {f}\n")

if __name__ == '__main__':
    display_info("John", 13)
    anotherFunc(3, (1,2), c=11, d=13)