from copy import deepcopy

#create a tuple
t1 = ("HELLO", 5, [], True) 
print(t1)
t2 = t1
print(f"t1=t2? {t1==t2}")
#make a copy of a tuple using deepcopy() function
t1_clone = deepcopy(t1)
print(t1==t1_clone)

print("Add 50 to the list at third item.")
t1_clone[2].append(50)
print(f"New clone of the tuple: {t1_clone}")
print(f"Original tupe: {t1}")
print(t1==t1_clone)
