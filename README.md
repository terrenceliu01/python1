# Python 1 class notes

## comment 
[comment](../src/languageBasics/../comment.py)
* single line comment: #
* multiple lines comment: """, '''

## Variable Naming
1. variable name cannot start with number
2. variable can be combination of letters and numbers _, a~z, A~Z, 0~9, no other special characters
3. don't use reserved keywords as variable name
![](images/python-keywords.png)
[Python Keywords](https://realpython.com/python-keywords/#:~:text=%20Python%20Keywords%20and%20Their%20Usage%20%201,are%20used%20for%20control%20flow%3A%20if%2C...%20More%20)
4. Avoid using existing function name as your variable name.
otherwise, your python builtins functions no longer works the way you expected.
### Variable and memory
![](images/chineseMedicine.jpg)
![](images/memory.gif)

## Data Type
* number
* string
* tuple
* list
* set
* dictionary

## Operator
* assignment
* bitwise
* comparison
* identity
* logical
* math
* membership
## Loop
* for loop
```
for <x> in <iterable variable>:
```
$$
\underbrace {for}_{keyword} x \underbrace {in}_{keyword} \space \space \underbrace {data}_{iterable} \underbrace {:}_{eol}
$$
* while loop
```  
  while <condition> :
```