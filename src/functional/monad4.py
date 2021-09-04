from pymonad.operators.maybe import Just, Nothing
from pymonad.reader import Compose

list1 = [1,2,3,4,5,6,7,8,9]
def head(alist):
    return [alist[0]]

def tail(alist):
    return alist[1:]

head1 = head(list1)
print(head1)

tail1 = tail(list1)
print(tail1)

newFunc = Compose(tail).then(head) # define all you want to do together
print(newFunc(list1)) # call then