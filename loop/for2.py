x = sum(i * i for i in range(10))
print(x)

v1 = (10, 20, 30)
v2 = (7, 5, 3)
l = list(zip(v1, v2))
print(l)
z = sum(x * y for x, y in zip(v1, v2))  # dot product
print(z)

# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
l = list(data[i] for i in range(len(data)-1, -1, -1))
print(l)