# Arithmatic Operator: +, -, *, /, %, //, **

a,b=30,20
print(a//b)

# Assignment Operator: =, +=, -=, */, /=, %=, //=
a += b

# Comparison Operator: ==, !=, >, <, >=, <=
c = a==b
print(c)

# Logical Operator: and, or
c = a>b and a>=b
print(c)

# Bitwise Operator: 
# & bit and
# | bit or
# ^ bit xor
# ~ not
# << shift left
# >> shift right

a = 0b00111100
b = 0b00001101
print(bin(a))
print("  "+bin(b))
print("  "+bin(a & b))

# membership operator: in, not in
l1 = [1,2,3,4,5]
print( 1 in l1)

# ternary operator:
a, b = 10, 20
min1 = a if a < b else b
print(min1)
max1 = a>b and a or b
print(max1)

# identity operator: is, is not
t1 = Turtle()
t2 = Turtle()
print(t1 is t2)

# other operator: **, *
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info,)
print(filename)

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(z)