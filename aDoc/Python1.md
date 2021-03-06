# Python level-I

## Table of Contents
- [Python level-I](#python-level-i)
  - [Table of Contents](#table-of-contents)
  - [Familiar with your keyboard](#familiar-with-your-keyboard)
  - [Using Markdown](#using-markdown)
  - [Getting start](#getting-start)
  - [playground and help document](#playground-and-help-document)
  - [print](#print)
  - [Data Type](#data-type)
  - [Operators](#operators)
  - [If-Else Execution Control](#if-else-execution-control)
  - [Loop](#loop)
  - [turtle](#turtle)
  - [draw snow man](#draw-snow-man)
  - [Function](#function)
  - [ball game](#ball-game)
  - [Simple math](#simple-math)
  - [Dice](#dice)
  - [Prime](#prime)
  - [Linear Algebra](#linear-algebra)
  - [Pandas DataFrame](#pandas-dataframe)
  - [Statistics Functions](#statistics-functions)
  - [numpy module](#numpy-module)
  - [File access](#file-access)
  - [plot](#plot)
  - [Python class](#python-class)
  - [OOP](#oop)
  - [install npm](#install-npm)
  - [ReactJS](#reactjs)
  - [App server](#app-server)
  - [Mongo DB](#mongo-db)
  - [Terminal Games](#terminal-games)
  - [Review](#review)
  - [install and using QuickType](#install-and-using-quicktype)
  - [Sqlite](#sqlite)
  - [tkinter GUI](#tkinter-gui)
  - [OpenGL](#opengl)

---
[Table of Contents](#table-of-contents)


## Familiar with your keyboard
![windows keyboard](./images/keyboard-windows.jpg)
![Apple keyboard](./images/keyboard-apple.jpg)

[Share Keyboard document](keyboard.md)

1. [Key name](https://www.computerhope.com/keys.htm)

    | Key   | Name                                                                     |
    | ----- | ------------------------------------------------------------------------ |
    | space | space, empty space in editor                                             |
    | Enter | return, enter, new line in editor                                        |
    | :     | colon, key:value separator in dict                                       |
    | ,     | comma, list or tuple item separator, delimiter in csv file               |
    | .     | dot, period, instance function call()                                    |
    | \#    | pound, hashtag, number, hold shift key click number 3, comments the line |
    | `     | back quote, grave accent, command block in markdown                      |
    | \*    | asterisk, star, bullet point in markdown, math multiply operator         |
    | ()    | parenthesis, tuple, function definition and call                         |
    | \-    | dash, hyphen, minus math operator, command option python --version       |
    | _     | underscore, dunder function or variable, private or protected variables  |
    | {}    | curly bracket, dict or set                                               |
    | []    | bracket, square bracket, list                                            |
    | \     | back slash, line continue, escape sequence                               |
    | /     | forward slash, file name path fold dilimiter                             |
    | \|    | pipe, virtical bar, bitwise OR operator                                  |
    | &     | ampersand, and simple, bitwise AND operator                              |
    | ^     | caret, circumflex, bitwise XOR operator                                  |
    | ?     | question mark, space holder in sqlit                                     |
    | $     | dollar sign                                                              |
    | ;     | semicolon                                                                |

* combination keys
```
    ctrl+c
    Ctrl+v
    ctrl+/
    shift+downarrow
    tab
    shift+tab
```
* Command line arrow key usage
```
    upArrow: bring previous command back
    downArrow: bring next command back
    leftArrow: move cursor to left in DOS window
    rightArrow: move cursor to right in DOS window
```
* Hight light block of code
* Ctrl+c: copy
* Ctrl+v: paste
* Ctrl+/: toggle comments

---
[Table of Contents](#table-of-contents)

## Using Markdown 
* turn in homework to GitHub
* VS Code Extension
    - Markdown All in One
    - Markdown Preview Enhanced
    - Unicode LaTex
* ??? Markdown md????????????????????????????????????
![???????????????????????????](./images/????????????.png)
    - add Markdown Extension
    - ???????????????????????? #, ##
    - ?????? bullet point *???1
    - ???????????????
    - ????????????
    - ????????????

![?????????????????????](./images/??????.jpeg)
* [Markdown Cheat Sheet](markdown-cheat-sheet.md)
* [Reference to pythonInstall.md](pythonInstall.md)
* Install Greenshot

    installation file name: Greenshot-INSTALLER-1.2.10.6-RELEASE.exe
* Basic operation    

---
[Table of Contents](#table-of-contents)

## Getting start
* install softwares needed

[refer to ](pythonInstall.md) python installation file.

* check installation
* installation check
```sh
python --version
git --version
code --version
```
* build working folders
```
mkdir workspace
cd workspace
mkdir python1
```
use text editor: NotePad.exe
```py
print("Hello, world!")
a = 4
b = 5
print(a+b)
```
save to first.py
```
python first.py
```
* build virtual environment

```
python -m venv env
```

![Virtual Environment](./images/virtualEnvironment.png)

* familiar with VSCode.
    [VS code](vscode.md)

* convert python script to exe
```
pip install pyinstaller
pyinstaller --onefile -w 'filename.py'
```

---
[Table of Contents](#table-of-contents)

## playground and help document
* python >>> help(print) (positional arguments, keyword arguments)
* [Practice]: different print statements
* hello/print.py
* hello/print-string.py
* [Practice]: Homework

---
[Table of Contents](#table-of-contents)

## print
* hello.py; getting start with Python > hello.ReadMe.md
* print.py; hello/print.py
* helloHim.py; intruduce input() function
* print-string.py; 
* input.py
* guessNumber.py
* dice.py; introduce random module, dice/dice1.py
* dice2.py; figure out possibility, understand how computer do things

![Special Characters](images/specialUnicode.png)

[Math Symbols](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols)

---
[Table of Contents](#table-of-contents)

## Data Type

![Three Basics](./images/LanguageBasics.svg)

* ![Data Type](./images/DataType.png)
* python terminal
* simpleDataType.py; simple datatype, number, string, boolean

    ![boolean conversion](./images/boolConversion.png)
* int, float, complex > floatTest.py
* str > strTest.py; operation on string
* tuple > tupleTest.py
* list > listTest.py

| list           | tuple             |
| -------------- | ----------------- |
| add data       | cannot be changed |
| remove data    | cannot be changed |
| change data    | immutable         |
| slow operation | made quickly      |

* tupleList.py 
    - create a list
    [expr for val in collection]
    [expr for val in collection if <condition>]
* set > setTest.py
    we use set when the order and frequency of data is not matter
    ```
    python >>>
    myset = set()
    dir(myset)
    help(myset.add)
    myset.add(1)
    myset.add("hello")
    myset.add(1)
    ```
    second time use myset.add(1) will be ignored.
    set do not contain duplicated element.
    
    ![Union of two set](./images/setUnion.png)

    ![Intersection of two set](./images/setIntersection.png)    

* dict > dictTest.py

[Basic date and time types](https://docs.python.org/3/library/datetime.html)

* datetime1.py; other data type (datetime.date)
* datetime2.py; difference between two dates
* strftime() and strptime() Format Codes
* datetime3.py; convert string to date
* datetime4.py; rocket launch date time.

| Directive | Meaning | Example |
| --------- |-----    |-------- |
| %a        | Weekday as locale???s abbreviated name.| Sun, Mon, ???, Sat (en_US);So, Mo, ???, Sa (de_DE)                               |
| %A        | Weekday as locale???s full name.| Sunday, Monday, ???, Saturday (en_US); Sonntag, Montag, ???, Samstag (de_DE)     |
| %w        | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.          | 0, 1, ???,6 |
| %d        | Day of the month as a zero-padded decimal number. | 01, 02, ???, 31 |
| %b        | Month as locale???s abbreviated name. | Jan, Feb, ???, Dec (en_US); Jan, Feb, ???, Dez (de_DE)|
| %B        | Month as locale???s full name.| January, February, ???, December (en_US); Januar, Februar, ???, Dezember (de_DE) |
| %m        | Month as a zero-padded decimal number.| 01, 02, ???, 12 |
| %y        | Year without century as a zero-padded decimal number.| 00, 01, ???, 99|
| %Y        | Year with century as a decimal number. | 0001, 0002, ???, 2013, 2014, ???, 9998, 9999|
| %H        | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, ???, 23|
| %I        | Hour (12-hour clock) as a zero-padded decimal number.| 01, 02, ???, 12|
| %p        | Locale???s equivalent of either AM or PM.| AM, PM (en_US); am, pm (de_DE)  |
| %M        | Minute as a zero-padded decimal number.| 00, 01, ???, 59|
| %S        | Second as a zero-padded decimal number.| 00, 01, ???, 59|
| %f        | Microsecond as a decimal number, zero-padded on the left.| 000000, 000001, ???, 999999|
| %z        | UTC offset in the form ??HHMM[SS[.ffffff]] (empty string if the object is naive)| (empty), +0000, -0400, +1030, +063415, -030712.345216 |
| %Z        | Time zone name (empty string if the object is naive).| (empty), UTC, GMT|
| %j        | Day of the year as a zero-padded decimal number. | 001, 002, ???, 366|
| %U        | Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, ???, 53|
| %W        | Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.| 00, 01, ???, 53|
| %c        | Locale???s appropriate date and time representation.| Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE) |
| %x        | Locale???s appropriate date representation. | 08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE)|
| %X        | Locale???s appropriate time representation. | 21:30:00 (en_US); 21:30:00 (de_DE) |
| %%        | A literal '%' character.|  |
| %G        | ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V)| 0001, 0002, ???, 2013, 2014, ???, 9998, 9999|
| %u        | ISO 8601 weekday as a decimal number where 1 is Monday.| 1, 2, ???, 7  |
| %V        | ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.| 01, 02, ???, 53 |

* datetime3.py; convert string to datetime by strptime(string, format)
* datetime4.py; differences between datetime, date, time
  
---
[Table of Contents](#table-of-contents)

## Operators
./operator

* Arithmetic Operators (+, -, *, /, %, **, //)
* 
[Arithmetic Operator](../operator/mathOperator.py)

| Operator | Name           | Example |
| -------- | -------------- | ------- |
| +        | Addition       | a + b   |
| -        | Subtraction    | a - b   |
| *        | Multiplication | a * b   |
| /        | Division       | a / b   |
| %        | Modulus        | a % b   |
| **       | Exponentiation | a ** b  |
| //       | Floor division | a // b  |

* Bitwise Operators

[bitwise sample code](../operator/bitwise.py)

| Operator | Name   |Description  |
|--------  |---     |------------ |
| &        | AND                  | Sets each bit to 1 if both bits are 1                                                                   |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                                                              |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1                                                         |
| ~        | NOT                  | Inverts all the bits                                                                                    |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |


* Assignment Operators

[Assignment sample code](../operator/assignment.py)

| Operator | Example | Same As |
| -------- | ------- | ------- |
| =        | x = 5   | x=5     |
| +=       | x += 3  | x=x+3   |
| -=       | x -= 4  | x=x-4   |
| *=       | x *= 5  | x=x*5   |
| /=       | x /= 4  | x=x/4   |
| %=       | x %= 5  | x=x%5   |
| //=      | x //= 3 | x=x//3  |
| \**=     | x \**= 2| x=x**2  |
| &=       | x &= 4  | x=x&4   |
| \|=      | x \|= 3 | x=x\|3  |
| ^=       | x ^= 4  | x=x^4   |
| >>=      | x >>=3  | x=x>>3  |
| <<=      | x <<=2  | x=x<<2  |

* Comparison Operators

[Comparison Sample code](../operator/comparison.py)

| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal                    | a == b  |
| !=       | Not Equal                | a != b  |
| <        | Less than                | a < b   |
| >        | Greater than             | a > b   |
| >=       | Greater than or equal to | a >= b  |
| <=       | Less than or equal to    | a <= b  |
  
* Logical Operators

[Logical Sample code](../operator/logical.py)

| Operator | Description                                   | Example        |
| -------- | --------------------------------------------- | -------------- |
| and      | Returns True if both statements are true      | a<5 and a>10   |
| or       | Returns True if one of the statements is true | x < 5 or x < 4 |
| not      | Reverse the returns                           | not (x<10)     |

* Identity Operators

[Identity Sample Code](../operator/identity.py)

| Operator | Description  | Example    |
|--------  |------------- | ---------- |
| is       | Returns True if both variables are the same object|a is b|
| is not   | Returns True if both variables are not the same object |a is not b |

* Membership Operators

[Membership Sample Code](../operator/membership.py)

| Operator |Description    | Example    |
| -------- | ------------- | ---------- |
| in       | Returns True if a sequence with the specified value is present in the object     | a in y     |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |

* Ternary Operators

[Ternary Sample Code](../operator/ternary.py)

if-else Statement structure:
```py
value_if_true if condition else value_if_false
```
Statement example:
```py
a = 5
s = "Hello" if a==5 else "A is not 5."
```
logical Statement:

```py
a=5
b=11
min1 = a<b and a or b
print(min1)
```
tuple statement
```py
min1 = (b, a)[a < b]
```

---
[Table of Contents](#table-of-contents)

## If-Else Execution Control
![If-Else](./images/IfElse.svg)

./if-else
* [Sample 1](../if-else/if-else1.py)
* [Sample 2](../if-else/if-else2.py) 
* [Sample 3](../if-else/if-else3.py)  
    - Infinit loop while True: > input("Continue? (y/n)")
    - [Practice]:
```output
2, 4, 6, 8, 10
1, 3, 5, 7, 9

```

---
[Table of Contents](#table-of-contents)

## Loop
![Loop-Continue-Break](./images/Loop.svg)
* forLoop1.py
* forBreak.py
* forContinue.py
* forNested1.py; print right triangle
* forNested2.py; print Equilatera triangle
* forNested3.py???print diamond
* forNested4.py; define function for n
* forElse.py
* for1.py; generator
* for2.py; more generator
* while.py
    - [Practice]: 
        ```output
        We're on time 0
        We're on time 1
        We're on time 2
        We're on time 3
        ```
    - loop string
* whileElse.py

![Do-While](images/DoWhile.svg)

* guessNumber.py
    - assign homework to modify guessNumber.py for two players

---
[Table of Contents](#table-of-contents)

## turtle

```
python -m turtledemo
```
* turtle1.py; display turtle pen 
* turtle2.py; basic turtle move 
* turtle3.py; mouse click on turtle 
* turtle4.py; random move on click 
* turtle5.py; avoid turtle move out of window
* turtle6.py; avoid turtle move out of window
* turtle7.py; display card on turtle screen
* turtle8.py; draw star
* turtle9.py; draw half circle
* shapes.py; triangle, rectangle, line, circle
* testShapes.py; test all functions defined in shapes.py
* drawSun.py; drawing a sun and house by using shapes.py
    - assign homework draw snow couple

    ![Snow Couple](./images/snowCouple.png)
---
[Table of Contents](#table-of-contents)

## draw snow man
* ![Snow Couple](./images/snowCouple.png)
* demo draw_snowman.py
* shapes.py
* testShapes.py
* drawSun.py; add snow man in the picture.
* homework> draw snowcouple

---
[Table of Contents](#table-of-contents)

## Function

![Built in functions](./images/builtinFunctions.png)
* define a function
$$
\underbrace {def}_{keyword} \underbrace {circle \_area}_{function \space name} \left(\underbrace {a, b,c ...}_{positional\; args} * \underbrace {e=None, f=200}_{keyword\;args}\right) \underbrace {:}_{eol}
$$
* type following code in python playground.
```py
def circleArea(radius):
    return 3.141593 * radius**2

def f():
    pass

dir()

f()

f

```

$$
area = \pi * r^2
$$

if you don't return value from function, you will get None when you assign the value to a variable.
* math1.py (circle area, rectangule area, triangle area)
* defineFunction.py (help(sum))
* collision.py; use / to avoid collision, 
* keywordArgs.py; positional arguments first
* practice: define a function with keyword arguments 
    - (createList.py parseString(str, sep=','))
* defaultValue.py
* annotation1.py; wonderful use of keyword arguments 
* annotation2.py; long large function
* ask.pys
* attribute.py
* optionalPositionalArgs.py
* innerFunction0.py
* innerFUnction1.py
* [homework1](../function/homework1.md)
* [homework2](../function/homework2.md)

---
[Table of Contents](#table-of-contents)

## ball game
* ball1.py [Display a ball at center of the screen.]
* ball2.py [Display a ball at the screen bottom]
* ball3.py [Use left/right arrow key to control the ball]
* ball4.py [Use space key to fire the ball]
* ball5.py [Move the ball gradually on fire.]
* ball6.py [put ball back when it moves out of the screen]
* ball7.py [Display bird and background.]
* ball8.py [Move the bird from right to left.]
* ball9.py [Move the bird back to start position once it is hitted.]
* ball10.py [Final version of ball game.]

---
[Table of Contents](#table-of-contents)

## Simple math
./mymath

![Built-in Functions](./images/builtinFunctions.png)
* math0.py/ built-in functions, abs(), pow(), sum(), max(), min(), round()

Square Root
$$
x=\sqrt x^2=x ^ \frac 1 2
$$
$$
4=\sqrt {16}=16 ^ \frac 1 2
$$
* [math1.py](../mymath/math1.py); functions defined in math module, sqrt(), ceil(), floor(), sin(), cos()
* [math2.py](../mymath/math2.py)
* [math2.py](../mymath/math10.py)
* [solution.py](../mymath/solution.py)

$$
A=\pi r^2
$$
, where **A** is area of a circle, **r** is radius of the circle.
* circle.py

* perfactNumber1.py
* Volumn of Sphere
$$
V = \frac 4 3 \pi  r^3
$$

* Volumn of Cylinder
$$
V = r^2 \pi \cdot h
$$

* Triangle area
  $$
  area = \frac 1 2 (b \cdot h)
  $$

$$\cdots  $$

* Triangular Number
  $$
  T_n = \sum_{k=1}^n k
  $$

  $T(n)=\frac {n(n+1)} 2$

![Triangular Number](./images/triangularNumber.png)
* solution1.py
* circle.py
* prime1.py; ./prime/prime1.py
* prime1.py ~ prim7.py; treat computer as humanbeen, do it right

More Exercises:
[Exercises and Solutions](https://www.w3resource.com/python-exercises/math/index.php)

---
[Table of Contents](#table-of-contents)

## Dice
* dice.py; introduce random module, dice/dice1.py
* dice2.py; figure out possibility, understand how computer do things

---
[Table of Contents](#table-of-contents)

## Prime
* prime0.py > straight forward, define function
* prime1.py > optimized by half
* prime2.py > define function isPrime()
* prime3.py > calculate range(40-50)
* prime4.py > define function rangePrime(x,y)

## Linear Algebra

![??????](./images/??????.jpg)

????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
* linear1.py; ?????????????????????
  
![Chicken & Rabbits](images/chickenRabbits.gif)

???????????????32?????????100 ?????????????????????????????????

* linear2.py
* linear3.py
* linear4.py
* linear5.py

## Pandas DataFrame
* pandas1.py; create DataFrame from .csv file, and plot
* pandas2.py; understand DataFrame
* pandas3.py
* pandas4.py
* pandas5.py

## Statistics Functions
* statistics1.py; mean() & fmean()
* statistics2.py; geometric_mean()
    $$Geometric\_mean=(x_1 x_2 x_3 \dots x_n)^{\frac 1 n}$$
* statistics3.py; harmonic_mean()
    $$Harmonic\_mean = \frac n {\sum_{i=1}^n \frac 1 {x_i}}$$
* statistics4.py; median(), median_low, median_high
* statistics5.py;
* statistics5.py;
* statistics7.py; pstdv() Population standard diviation

    $$\sigma = \sqrt {\frac 1 N \sum_{i=1}^N (x_i-\mu)^2}$$
    , where
    
    $\sigma \to$ Population Standard Diviation

    $N \to$ Total number of population elements

    $\mu \to$ Population mean

    Sample Variance Formula:
    $$s ^2 = \frac 1 {n-1} \sum_{i=1}^n (x_i-\bar{x})^2$$
   , where
    
    $s^2 \to$ sample variance
    $x_i \to$ value of ith element

    $n \to$ sample size

    $\bar{x} \to$ sample mean

* statistics8.py; stdev(), variance

    $$\mu=\frac {\sum {x}} N$$
    $$\bar {x} = \frac {\sum {x}} n$$
    where N represent number of population, and n represent size of a sample.
* statistics9.py; NormalDist class

## numpy module
[numpy module Tutorial](https://numpy.org/devdocs/user/tutorials_index.html)

* numpy1.py; underatand numpy array
* numpy2.py; plot sin(x) wave
* numpy3.py; Arithmetic operators on arrays apply elementwise.
* numpy4.py; 2D array and linear algebra solution
* numpy5.py; Universal Functions
* numpy6.py; Array Indexing, Slicing and Iterating
* numpy7.py; image of the Mandelbrot fractal
* numpy8.py; normalized histogram

---
[Table of Contents](#table-of-contents)

## File access

| Text Files                                    | Binary Files                                              |
| --------------------------------------------- | --------------------------------------------------------- |
| Plain Text, XML, HTML, JSON, Source Code, CSV | Compiled code, App data, Media files, images,audio, video |

* file0.py (write to file)
* file1.py (read and write to existing file)
* file2.py (with open, auto close)
* file3.py (dump json, write to json file)
* file3a.py (read json from file)
* file3b.py (read json from string)
* file4.py (pandas read csv)
* file5.py (read csv file, and plot the data)
* file6.py (write dict to csv file)
* readJson.py
* csvReader.py

---
[Table of Contents](#table-of-contents)

## plot
* plot0.py
* plot1.py
* plot2.py
* plot3.py
* plot-student-csv.py
* [Practice]: plot sin(x) and cos(x) in the same chart > plot4.py
* China-vs-USA.py
    - [Online data](https://open-covid-19.github.io/data/data.csv)
    - [Online data](https://open-covid-19.github.io/data/data_minimal.csv)
    - [Homework] Choose different two states, plot the data
* covid-19/covid0.py
* covid-19/covid1.py
* covid-19/covid2.py

[Animations with Matplotlib](https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c)

  * movingSinWave.py
    ![Moving Sine Wave](../plot/../sine_wave.gif)
  * growingCoil.py
    ![Drawing coil](../plot/../coil.gif)
  * stockDynamic.py & stock.txt
  * 3dAnimation.py

[Download ImageMagick](https://imagemagick.org/script/download.php)
Install Magic by running file:

ImageMagick-x86_64-pc-windows.exe

after installation finished check the installation:

```
magick logo: logo.gif
magick identify logo.gif
magick logo.gif win:

magick -delay 10 Volcano_*.png volcano.gif
```
The animated gif file will be created.

![3D animation](../plot/volcano.gif)

[Matplotlib Exercises and Solution](https://www.w3resource.com/graphics/matplotlib/basic/index.php)

---
[Table of Contents](#table-of-contents)
    
## Python class
```py
class User:
    pass
```
* assign fields to an instance of User

[Python Classes](https://www.w3schools.com/python/python_classes.asp)
 
* person.py 
* bookdb.py
* create a class snowman.py > drawSnowMan.py > shapes.py
* [x] class0.py - pass class, instance and class level attributes
* [x] create a class snowman.py > drawSnowMan.py > shapes.py
* [x] class1.py > dynamically assign instance attribute and access it from outside function
* [x] class2.py > define internal function
* [x] class3.py > __init__(self) and internal function
* [x] class4.py > use keyword argument in __init__(self)
* [x] class5.py > understand __str__, __repr__, and __len__()
* [ ] class6.py > protected attribute and private attribute
* [ ] class7.py > getter/setter
* [ ] class8.py; inherite from Enum
* [ ] class9.py; difference between __init__ and __new__
* [ ] class10.py; override __new__() constructor
* [ ] class11.py; issue caused by class level variables
* [ ] class12.py; different object with different attributes
* [ ] class13.py; class level variables
* [ ] class14.py; define internal function by outside function, the benifit is use this outside function by more than one class.
* [ ] class15.py; function call function
* [ ] class16.py; multiple inheritance
* [ ] class17.py; reverse given string
* [ ] class18.py; define Website class
 
* [ ] personInheritance.py > inheritance
* [ ] personTest.py > understand class name <module_name>.<class_name>
* [ ] bookdb.py > used in app4.py
* [ ] polygon.py; ask student implement __repr__(self)
* [ ] student.py; using class level method
* [ ] snowman.py & drawSnowMan.py; draw snowman with class

---
[Table of Contents](#table-of-contents)

## OOP  
![OOP concept](./images/classDefine.png)
- class book, __init__, __repr__
- class student.py constructor, __repr__ abstraction
![class abstract](./images/classAbstraction.png)
- user.py, User, SubUser inheritence testUser
- person, teacher, student inheritence
![Person<Student](./images/student.png)
[YouTube Classes](https://www.youtube.com/watch?v=apACNr7DC_s)
[Python Classes](https://docs.python.org/3/tutorial/classes.html)

--- 
[Table of Contents](#table-of-contents)

## install npm
[Download and install node](https://nodejs.org/en/download/)
![Download image](./images/nodeDownload.png)
    - windows File: node-v12.18.3-x64.msi
    - macos File: 
* Install NodeJS & npm on windows 10
[nodejs.org/en/](https://nodejs.org/en/)

![install page](./images/nodeInstall.png)

Google Search: install reactjs on windows 10

[Step by step](https://www.liquidweb.com/kb/install-react-js-windows/) option 2

```
node --version
npm --version
```
* create react js application
```
npm install -g create-react-app

create-react-app --version

create-react-app reactproject2
```

* Install ReactJs on MacOS

```
sudo npx create-react-app wang-app
sudo chown -R wangqianjiang wang-app
cd wang-app
npm start
```

---
[Table of Contents](#table-of-contents)

## ReactJS
* web application vs. window application
open new VSCode window > python-gui (demo on window's machine.)
```
python calculator2.py
```

![Python Web Application](images/PythonWebApp.png)
* get reactjs project from github
```
git clone https://github.com/jwang1122/reactjs.git
```
* start the application
open new VSCode > ~/workspace/reactjs

```
cd server
python app.py
cd ../book-app
npm start
```

---
[Table of Contents](#table-of-contents)

## App server
* URL: Uniform Resource Locator
    - https://www.google.com
    - Protocal: http, https, ftp ...
    - Host: www.google.com
    - Port: number followed by :, default 80 for http, 443 for https
    - Path: 
    - Querystring: text after ?, key=value pair separated by &
    - Fragment: text after #(hashtag), jump to certain section in the document 

* app1.py > ping-pong
* app2.py > <html>
* app3.py > display hardcoded books
* app4.py > display books from mongodb, postman > test service
* getJson.py > load books from given website url

* bookdb.py
* Install Postman
    [Download Website](https://www.postman.com/downloads/)
    ![First time run Postman](images/postman.png)
* start app4.py, test POST, UPDATE, DELETE methods

---
[Table of Contents](#table-of-contents)

## Mongo DB

[Install MongoDB](MongoDB.md)
* NoSQL - MongoDB -> 
    - [collection](images/collections.png)
* SQL: Structured Query Language
[What is SQL?](https://www.w3schools.com/sql/sql_intro.asp)

* create0.py > create book and save it to mongodb
* create1.py > create more than one document at once
* retrieve0.py > retrieve one book from mongodb
* retrieve1.py > retrieve all books from mongodb
* retrieve2.py > retrieve some books based on condition from mongodb
* update.py > update one document 
* delete.py > delete one document
* bookdb.py > create a class include all CRUD process.

---
[Table of Contents](#table-of-contents)

## Terminal Games
* Check homework
* roll dice
    - dice.py
    - [Practice]: add total value of 2 dices
    - [Practice]: circle.py > circle_area(r)
* guess number
    - guessNumber.py
* ball game
    ball10.py

---
[Table of Contents](#table-of-contents)


## Review
* Markdown document
* ball game
* draw snowman
* file access (read/write plain text, csv, json)
* plot
* covid_19
* debug python code
* database access (CRUD)
* Postman to test web service
* application web server
* react JS front end GUI server

---
[Table of Contents](#table-of-contents)

## install and using QuickType
[QuickType website](https://quicktype.io/)

* QuickType Installation

```
npm install -g quicktype
quicktype --version
```

* Python code generation
```
quicktype ./data/student.json -o student.py
```
* install
```
npm intall -g quicktype
quicktype --version
```
* generate python code based on Json
```
quicktype ./data/student.json -o student.py
```
* book.py > __init__, __str__
* student.py constructor, __repr__ abstraction

* user.py, User, SubUser inheritence testUser
* person, teacher, student inheritence

[YouTube Classes](https://www.youtube.com/watch?v=apACNr7DC_s)

classes are foundmantal tools to any object oriented programing language, think of class as template for creating object and related data and functions that do interesting things with that data. Python make it easy to create classes

---
[Table of Contents](#table-of-contents)

## Sqlite
* sqlite0.py > create connection
* sqlite1.py
* sqlite2.py
* install DB browser for SQLite

Google Search: DB Browser for Sqlite

[SQLite GUI Download Website](https://sqlitebrowser.org/dl/)

[SQLite Browser for MacOS](https://sqlitebrowser.org/blog/macos-installer-rebuilt-for-3-11-1/)

File: DB.Browser.for.SQLite-3.12.1-win64-v2.msi
![Runing Image](images/sqlite.png)
* sqlite4.py
* sqlite5.py
* sqlite6.py

![Relation between Project and tasks](./images/entity.png)

* sqlite7.py > build relational data
* sqlite8.py > show relation between project and task

![projects - tasks](images/projects-tasks.png)

* review bookdb.py
* sqlite9.py > create books table
* sqlite10.py > insert data into books table
* sqlitebookdb.py > build CRUD
* app5.py > use sqlitebookdb.py to provide service
    use Postman to check the service.

---
[Table of Contents](#table-of-contents)

## tkinter GUI
[tkinter documentation](https://docs.python.org/3/library/tk.html)
[tkinter course](https://www.python-course.eu/tkinter_menus.php)
[tkinter sample web](https://pythonlobby.com/introduction-to-python-gui-using-tkinter)

|Basic Widgets|
|---          |
|Buttons      |
|Labels       |
|Frames       |
|CheckBoxes   |
|RadioButtons |
|Entry        |
|ComboBox     |


- [ ] tkinter1.py; tkinter.TK() Open window
- [ ] tkinter2.py; add Label
- [ ] tkinter3.py; disable resize window
- [ ] tkinter4.py; Exit Button
- [ ] tkinter5.py; add line to Canvas
- [ ] tkinter6.py; Button with command function
- [ ] tkinter7.py; Combobox
- [ ] tkinter8.py; Checkbutton
- [ ] tkinter9.py; Spinbox
- [ ] tkinter10.py; Text
- [ ] tkinter11.py; Entry
- [ ] tkinter12.py; Radiobutton
- [ ] tkinter13.py; Radiobutton
- [ ] tkinter14.py; ScrolledText
- [ ] tkinter15.py; Progressbar
- [ ] tkinter16.py; Disable button
- [ ] tkinter17.py; Listbox
- [ ] tkinter18.py; Listbox
- [ ] tkinter19.py; Simpledialog
- [ ] tkinter20.py; Inheritence from tkinter.Frame
- [ ] tkinter21.py; Display resized image in frame
- [ ] tkinter22.py; Select file from file explore
- [ ] tkinter23.py; Read file and display contents in Scrolledtext
- [ ] tkinter24.py; Read file and save contents in Scrolledtext to a file
- [ ] tkinter25.py; Menu
- [ ] tkinter26.py; Layout management: pack()
- [ ] tkinter27.py; Layout management: pack(fill=tk.X)
- [ ] tkinter28.py; Layout management: pack(fill=tk.X, padx=10)
- [ ] tkinter29.py; Layout management: pack(fill=tk.X, pady=10)
- [ ] tkinter30.py; Layout management: pack(fill=tk.X, pady=10, side=tk.LEFT)
- [ ] tkinter31.py; Layout management: place(x, y, width, height)
- [ ] tkinter32.py; Layout management: grid(row, column)
- [ ] tkinter33.py; Button.bind and event
    [Bind & event](https://www.python-course.eu/tkinter_events_binds.php)
- [ ] tkinter34.py; Mouse position (event.x, event.y)
- [ ] tkinter35.py; Table
- [ ] tkinter36.py; Pie chart
- [ ] tkinter37.py; page switch and animated chart
- [ ] tkinter38.py; Notebook (tabs)
- [ ] tkinter39.py; LabelFrame (titled frame)

<table border="1">
<tr>
<th>Event</th>	<th>Description</th>
<tr><td>
Button	</td><td>A mouse button is pressed with the mouse pointer over the widget. The detail part specifies which button, e.g. The left mouse button is defined by the event "Button-1" the middle button by 'Button-2', and the rightmost mouse button by 'Button-3'.
'Button-4' defines the scroll up event on mice with wheel support and and 'Button-5' the scroll down.
If you press down a mouse button over a widget and keep it pressed, Tkinter will automatically "grab" the mouse pointer. Further mouse events like Motion and Release events will be sent to the current widget, even if the mouse is moved outside the current widget. The current position, relative to the widget, of the mouse pointer is provided in the x and y members of the event object passed to the callback. You can use ButtonPress instead of Button, or even leave it out completely: , , and '1' are all synonyms.</td>
</tr>
<tr>
<td>Motion</td>
<td>The mouse is moved with a mouse button being held down. To specify the left, middle or right mouse button use <B1-Motion>, <B2-Motion> and <B3-Motion> respectively. The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback, i.e. event.x, event.y</td>
</tr>
<tr>
<td>ButtonRelease</td>
<td>Event, if a button is released. To specify the left, middle or right mouse button use 'ButtonRelease-1', 'ButtonRelease-2', and 'ButtonRelease-3' respectively. The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback, i.e. event.x, event.y</td>
</tr>
<tr>
<td>Double-Button</td>
<td>Similar to the Button event, see above, but the button is double clicked instead of a single click. To specify the left, middle or right mouse button use 'Double-Button-1', 'Double-Button-2', and 'Double-Button-3' respectively.
You can use Double or Triple as prefixes. Note that if you bind to both a single click ('Button-1') and a double click ('Double-Button-1'), both bindings will be called.</td>
</tr>
<tr>
<td>Enter</td>
<td>The mouse pointer entered the widget.
Attention: This doesn't mean that the user pressed the Enter key!. <Return> is used for this purpose.</td>
</tr>
<tr>
<td>Leave</td>
<td>The mouse pointer left the widget.</td>
</tr>
<tr>
<td>FocusIn</td>
<td>Keyboard focus was moved to this widget, or to a child of this widget.</td>
</tr>
<tr>
<td>FocusOut</td>
<td>Keyboard focus was moved from this widget to another widget.</td>
</tr>
<tr>
<td>Return</td>
<td>The user pressed the Enter key. You can bind to virtually all keys on the keyboard: The special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.</td>
</tr>
<tr>
<td>Return</td>
<td>The user pressed the Enter key. You can bind to virtually all keys on the keyboard: The special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.</td>
</tr>
<tr>
<td>Key</td>
<td>The user pressed any key. The key is provided in the char member of the event object passed to the callback (this is an empty string for special keys).</td>
</tr>
<tr>
<td>a</td>
<td>The user typed an "a" key. Most printable characters can be used as is. The exceptions are space ('space') and less than ('less'). Note that 1 is a keyboard binding, while '1' is a button binding.</td>
</tr>
<tr>
<td>Shift-Up</td>
<td>The user pressed the Up arrow, while holding the Shift key pressed. You can use prefixes like Alt, Shift, and Control.</td>
</tr>
<tr>
<td>Configure</td>
<td>The size of the widget changed. The new size is provided in the width and height attributes of the event object passed to the callback. On some platforms, it can mean that the location changed.</td>
</tr>
</table>

## OpenGL

Install PyOpenGL modules

```
pip install PyOpenGL PyOpenGL_accelerate
```

[OpenGL Tutorial](https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/)

* [ ] opengl1.py; rotate Cube with edge lines only
* [ ] opengl2.py; rotate Cube with colored surface and lines
* [ ] opengl3.py; move Cube by arrow keys or mouse wheel
* [ ] opengl4.py; move Cube by arrow keys or mouse wheel
* [ ] opengl5.py; move Cube by arrow keys or mouse wheel
* [ ] opengl6.py; move Cube by arrow keys or mouse wheel