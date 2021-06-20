tuple1 = ()
print(tuple1)
print(type(tuple1))
tuple2 = tuple()
print("Using tuple() function:",tuple2)
tuple2 = 1, 3, 34,"hello", "world"
# list2 = list(tuple2)
# tuple2 = list(list2) + ["hello", "world"]
# tuple2 = tuple(tuple2)
print(tuple2)
# list3 = []
list3 = [i for i in range(9) if i%2==0]
    
print("Using for-in operator:",tuple(list3))
