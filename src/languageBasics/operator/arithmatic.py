# Math Operators +;-;*;/;%;**;//
a, b = 20, 30
c = a + b
d = a - b
e = a * b
f = a / b

print("08:", b % a) # modulus
print("09:", 2**4) # exponential
# Floor Division
print("11:", 9 // 2)  # 4
print("12:", 11 // 3)  # 3
print("13:", -11 // 3)  # -4

# Why we need // operator
a = 20
b = 3
# c = a/b
c = a//b
print(type(c))
for i in range(c):
    print(i, end=' ')