from datetime import date
today = date.today()

a, b = 5, 9
c = a+b
print("06. %d + %d = %d" % (a, b, c))

name, age = "John", 16
print("09. Hello,", name + "!")
print("10. Hello, %s!" % name)
print("11. Hello, {0}!".format(name))
print(f"12. Today is {today}. Hello, {name}")
print("13. Today is {1}. Hello, {0}!".format(name, today))
print("14. %s is %d years old." % (name, age))
print("15.", name, "is", age, "years old.")
person = (name, age)
print("17. %s is %d years old." % person)

pi = 3.1415926
print("20. pi is %4.3f" % pi)
print(f"21. pi is {pi:4.3f}")

data = ("John", "Doe", 53.446826374)
format_string = "23. Hello %s %s. Your current balance is $%.2f"
print(format_string % data)

print("::".join("abc"))

face = "A"
suit = "Diamonds"
print(" of ".join((face,suit)))
