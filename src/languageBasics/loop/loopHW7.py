n = 6
for num in range(1, n):
    print(' '*(n-num), end='')
    print((str(num)+' ') * num)

for num in range(n-2, 0, -1):
    print(' '*(n-num), end='')
    print((str(num)+' ') * num)

for i in range(5):
    for x in range(5-i):
        print(" ", end="")
    for j in range(0, i+1):
        print(i+1, end=" ")
    print()

for i in range(4, 0, -1):
    for x in range(6-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(i, end=" ")
    print()
