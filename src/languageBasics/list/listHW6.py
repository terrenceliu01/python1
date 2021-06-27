list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

l = list(filter(None, list1)) # Use a filter() function to remove None type from the list
print(l)

l = list(filter(lambda x: len(x)!=0, list1))
print(l)