"""
Understandf my wrapper function
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

def display_info(name, age):
    time.sleep(2)
    print(f"display_info()... ran with arguments: ({name}, {age})")

if __name__ == '__main__':
    display_info = my_timer(display_info)
    display_info("John", 13)