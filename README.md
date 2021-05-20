# Python 1 class notes

## github
* Clone source code from github.
In Terminal, change to target workspace folder, and do following command,
```
git clone <url copied from github>
git clone https://github.com/terrenceliu01/python1.git
```
* Check GIT status
```
git status
git log --oneline
git branch
git branch <new branch>
```
* Config GIT user and email
```
git config user.name <'username'>
git config user.email <'email'>
git init
```
* Git revision
```
git checkout <revision>
git checkout <branch>
git checkout master
git merge dev
git tag
git tag -a <tag number> -m <"tag message">
git tag -a v1.4 -m "my version 1.4"
```

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