"""
override __iter__, __next__ function
"""
class Reverse:
    def __init__(self, data): # data is iterable
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

if __name__ == '__main__':
    s = Reverse("international")
    for c in s:
        print(c, end="")
    print()

    s = Reverse("international")
    print(next(s))
    print(next(s))

    for i in range(10):
        print(i)