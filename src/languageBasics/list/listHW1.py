aList = [100, 200, 300, 400, 500]

l = []
for i in range(len(aList)-1, -1, -1):
    l.append(aList[i])

print(l)

l = aList[::-1]
print(l)

aList.reverse()
print(aList)