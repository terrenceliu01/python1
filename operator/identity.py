import turtle

a = 5
b = 5
c = a

print(a is b)
print(a is c)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = t1

print(f"t1 is t2: {t1 is t2}")
print(f"ti is t3: {t1 is t3}")
print(f"t1 is not t2: {t1 is not t2}")
