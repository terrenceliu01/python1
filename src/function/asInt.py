def asInt(number):
    return int(number)


def test():
    assert asInt('1') ==1, "I got big problem!!!!"
    assert asInt('2') ==2, "I got big problem!!!!"


if __name__ == '__main__':
    test()
    print("Done.")
    