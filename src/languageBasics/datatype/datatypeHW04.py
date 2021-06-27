#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex, end="\n\n")
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print("Add 9 to the tuple: ")
print(tuplex, end="\n\n")
#adding items in a specific index
print("Insert (15, 20, 25) at index=5: ")
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[5:]
print(tuplex, end="\n\n")
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx[4] = 30
tuplex = tuple(listx)
print(f"Change value 3 to 30: {tuplex}")
