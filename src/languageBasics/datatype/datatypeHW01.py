#Create an empty tuple 
x = ()
print(f"An empty tuple: {x}")
print(type(x))

#Create an empty tuple with tuple() function built-in Python
tuple1 = tuple()
print(f"Using tuple() function: {tuple1}")

# Create a tuple with different data type elements
t1 = (1, 3, 34, "Hello", "World")
print(t1)

t1 = tuple([value for value in range(10) if value%2==0])
print(f"Using for-in operator: {t1}")