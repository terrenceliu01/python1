"""
@classmethod vs. @staticmethod
1. both can be called by class name
2. @classmethod has first cls possitional argument, @staticmethod has no this first argument
"""

class C:
    classAttribute = 10

    @classmethod
    def f1(cls, *args):
        print(cls.classAttribute)
        print(args)

    @staticmethod
    def f2(**keyargs):
        print(C.classAttribute)
        print(keyargs)

if __name__ == '__main__':
    C.f1(1,2,3,4)
    C.f2(name="John", occupation="teacher")

