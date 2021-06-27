* Write a Python program to use of frozensets.

Note: Frozensets behave just like sets except they are immutable.

for given two set:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

1. make sure you cannot modify these two set.
2. make sure there are some items in common.
3. find elements which in set1 but not in set2.
4. merge these two sets together.

Expected output:

```
There is no common element in x and y:  False
The elements in x but not in y are:  frozenset({1, 2})
Merger x and y is:  frozenset({1, 2, 3, 4, 5, 6, 7})
```