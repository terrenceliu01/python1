"""
'yield' is similar to 'return', instead of return one value,
'yield' returns a squence of values.

 We should use yield when we want to iterate over a sequence, 
 but don’t want to store the entire sequence in memory.

 The yield statement suspends function’s execution and sends 
 a value back to the caller, but retains enough state to enable 
 function to resume where it is left off. When resumed, 
 the function continues execution immediately after the last 
 yield run. This allows its code to produce a series of values 
 over time, rather than computing them at once and sending 
 them back like a list.

 Above statement is little hard to understand, to make it easy,
 try to debug the yield python program.
"""
def simpleGeneratorFunc():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    g = simpleGeneratorFunc()
    print(g)
    for i in g:
        print(i)
