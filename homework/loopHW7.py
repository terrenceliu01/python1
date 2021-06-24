n = 6
k = n-1
for i in range (1,n):
    for j in range (1,k):
        print(end= " ")
    k = k-1
    for j in range (i):
        print(f"{i} ", end = "")
    print("\r", )

k = n-1
for i in range (n-2,0,-1):
    for j in range (n-i-1):
        print(end= " ")
    k = k-1
    for j in range (i):
        print(f"{i} ", end = "")
    print("\r", )
