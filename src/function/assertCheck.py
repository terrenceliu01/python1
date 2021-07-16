"""
assert check before calculation

assert: I swear this must be true, in case it happens, let me know
❌❗️Once it happens, you have big problem!
provide aid for developer find root cause.
not for handling run-time error.
😢only give you one kind of error which is AssertionError
"""

from math import pi

def circleArea(r):
    assert type(r) in [int, float], f"AssertionError: radius should be int or float, but radius={r}"
    return r ** 2 * pi


if __name__ == '__main__':
    try:
        x = circleArea(2-4j)
        print(x)
    except Exception as error:
        print(error)

    print("End")