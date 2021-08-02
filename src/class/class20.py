"""
inner class or nested classes
"""

class Outer: # composition vs. inheritance
    class Inner:
        pass
        class Inter_Inter:
            pass
    
if __name__ == '__main__':
    print(dir(Outer))
    print(type(Outer.Inner))