start = int(input("Please enter a start year: "))
end = int(input("Please enter a end year: "))

l = []
for i in range(start, end+1):
    if i%4==0:
        l.append(i)

print(f"the leap years between {start} and {end} are \n{l}\n")
