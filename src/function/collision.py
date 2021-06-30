"""
TypeError: foo() got multiple values for argument 'name'
"""
# def foo(name, firstName="John", lastName="Wang", name='John Wang'):
#     pass

def foo(name, **kwds):
    print(kwds)
    print(name)
    return 'name' in kwds # ask if there is key named 'name' in the dictionary

def foo1(name, /, **kwds): # In other words, the names of positional-only parameters can be used in **kwds without ambiguity.
    return 'name' in kwds

foo("john", firstName="John", lastName="Wang", fullname='John Wang')
# x = foo(1, **{'name': 2})
# #x = foo1(1, **{'name': 2})
# print(x)

