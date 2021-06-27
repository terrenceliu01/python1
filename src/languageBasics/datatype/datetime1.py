"""
Other than Python language intrisic data type,
python also built in a lot of other data type, such as datetime
"""
import datetime
"""
>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 
'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

birthday = datetime.date(1956,1,31) # Python creator Guido Van Rossum
print(birthday)
print(type(birthday))

a = 5
print(type(a)) # both datetime.date and int are Python class, there is no difference between

print(birthday.day)
print(birthday.month)
print(birthday.year)