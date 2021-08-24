temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26),("Tokyo", 27),("New York", 28),("London", 22),("Beijing", 32)]

c2f = lambda data: (data[0], round((9/5*data[1]+32), 0))

def mymap(f, data):
    result = []
    for d in data:
        x = f(d) # apply function to each element
        result.append(x)
    return result

x = mymap(c2f, temps)
print(x)