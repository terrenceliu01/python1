n = 6
k = n-1
for i in range (1,n):
    for j in range (1,k):
        print(end= " ")
    k = k-1
    for j in range (i):
        print(f"{i} ", end = "")
    print("\r", )
