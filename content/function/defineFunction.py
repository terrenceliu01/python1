def f(a, b, /, c, d, *, e=3, f="H"):
    """
    a,b are positional-only, c,d can be positional or keyword
    e and f are required to be keyword.
    / separate the position-only arguments from others
    * separate the keyword-only arguments from others

    dir(__builtins__)
    help(list)
    help(sorted)
    """
    print(a, b, c, d, e, f)
    return "Done."

if(__name__ == "__main__"):
    x = f(2, 4, "c", "d", e="9",f=6) # c,d as positional args
# print(x) # function has no return value retuens None.
# x = f(4, 2, d="d", c="c", e=9, f=10) # c,d now is keywords args
# x = f(4, 2, 4, e=9, f=10, d="d") # if c,d is keywords, can switch
# x = f(5, 6, 4, e=7, d="d", f=10) # 4 will be consider as c
# x = f(1, 2, 3, 4, 5, f=6) # e cannot be keyword argument
#__add__(self, value, /) # means, no keyword arguments allowed.
    print(x)