"""
Logical Operator: 

and: return True only both sides are True, return False otherwise  
or : return False only both sides are False, return True otherwise
not: return True two sides are not the same, return False otherwise
"""

a, b = 10, 20

c = (a == 60) and b == 13
print("12:", c)
c = (a == 60) and b < 13
print("14:", c)
c = (a == 60) or (b > 15)
print("16:", c)
c = (a < 60) or (b > 15)
print("18:", c)
min1 = a < b and a or b  # find which one is smaller
print("20:", min1)
max1 = a > b and a or b  # find which one is smaller
print("22:", max1)
c = a and b      # return b if a!=0, return 0 otherwise
print("24:", c)  # Strange result? c = a and b or a
c = a or b       # return a if a!=0, return b otherwise
print("26:", c)  # Strange result? c = a and a or b
