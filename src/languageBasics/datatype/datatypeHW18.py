l1 = [23, 43, 67, 12, 33, 41, 12, 43]
l2 = [1, 2, 3, 4, 5, 12, 43]
flag = False
for x in l1:
    for y in l2:
        if x==y:
            flag = True
            break

print(flag)

flag = True in {i==j for i in l1 for j in l2}
print(flag)

s1 = {i==j for i in l1 for j in l2}
print(s1)