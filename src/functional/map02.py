temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26),("Tokyo", 27),("New York", 28),("London", 22),("Beijing", 32)]

# normal loop to convert temperature
list1 = []
for data in temps:
    city = data[0]
    temp = round((9/5*data[1]+32), 0)
    list1.append((city, temp))

print(list1)

x = list(map(lambda data: (data[0], round((9/5*data[1]+32), 0)), temps)) # map get rid of loop
print(x)