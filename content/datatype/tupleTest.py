"""
list contains sequence of data separated by comma, surrounded by brackets.方数组
tuple is sequence of data separated by comma, surrounded by parentheses。圆数组
l = [2,3,5,7,9]
t = (1,4,9,16,25)
dir(l)
dir(t)
"""
#Empty tuple
tuplex = ()
tuplex = tuple()

# create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

survey = (21, "China", True)
print("Age: %d, Country: %s, Knows_python: %s" % survey)
age, country, knows_python = survey  # assign more values in one line.
print(f"Age = {age}")
print(f"Country = {country}")
print(f"Knows_python? {knows_python}")


# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)  # without , (9) treated as an int
print(tuplex)
# adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
# converting the tuple to list
listx = list(tuplex)
# use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)
# insert tuple at give position [3]
tuplex = tuplex[:3] + (9, 8, 7) + tuplex[3:]
print(tuplex)

a = (1, 2, 3)
b = (4, 5, 6)
c = tuple(zip(a, b))
print(c)

# a, b, c = (1, 2, 3, 4, 5)  # ValueError
# a, b, c = (3, 5)  # ValueError

# Why we need use tuple?

a1, a2, a3, a4, a5, a6 = 56, 78, 88, 76, 56, 89
average = (a1 + a2 + a3 + a4 + a5 + a6)/6
print(average)

tuple1 = 56, 78, 88, 76, 56, 89
average = sum(tuple1)/len(tuple1)
print(f'Average of the tuple1 is {average}.')

