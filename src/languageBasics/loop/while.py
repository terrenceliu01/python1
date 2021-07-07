a, b = 0, 1
while a < 10:
    print(a+b, end=' ')
    a, b = a+1, a+b
print()

# Use break to simulate do-while
i = 6
while True: # unconditional execution
    print(i, end=' ') # this part will be run at least once
    i += 1
    if i>5:
        break
print()

