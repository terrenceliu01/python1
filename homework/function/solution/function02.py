def mergeDict(entry_1, entry_2):
    """py
    Return a merged dictionary with two inputs
    """
    return {**entry_2, **entry_1}

if __name__ == '__main__':
    x = {"a": 1, "b": 2}
    y = {"b": 3, "c": 4}
    z = mergeDict(x,y)
    print(z)
