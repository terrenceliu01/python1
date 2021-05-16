startStr = input("Please enter a start number: ")
start = int(startStr)
endStr = input("Please enter a end number: ")
end = int(endStr)

numbers = range(start, end) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print(f"Number of even numbers :{count_even}")
print(f"Number of odd numbers  :{count_odd}")