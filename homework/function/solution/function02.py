def mergeDict(entry_1, entry_2):
    """py
    Return a merged dictionary with two inputs
    keep the first dict value if both of them has the same key
    """
    return {**entry_2, **entry_1}

if __name__ == '__main__':
    x = {"a": 1, "b": 2}
    y = {"b": 3, "c": 4}
    print(x)
    print(y)
    z = mergeDict(x,y)
    print(z)
