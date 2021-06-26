* Write python program to find out given range of leap years.

Sample output looks similiar as:
```
Please enter a start year: 2000
Please enter a end year: 2020
the leap years between 2000 and 2020 is 
[2000, 2004, 2008, 2012, 2016, 2020]
```

start = int(input("Please enter a start year: "))
end = int(input("Please enter a end year: "))

list1 = []
for i in range(start, end):
    if i%4==0:
        list1.append(i)

print(f"the leap years between {start} and {end} are {list1}")