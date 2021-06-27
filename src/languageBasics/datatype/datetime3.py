"""
Convert string to datetime.datetime (string-parse-to-time)
    - Module:   datetime
    - Class:    datetime
    - Function: strptime()
datetime.datetime.strptime(datestring:str, formatstring:str) -> datetime.datetime

Convert datetime to string (string-format-of-time)
    - Module:   datetime
    - Class:    datetime
    - Function: strftime()
datetime.datetime.strftime(date:datetime, format:str) -> str
datetimeobject.strftime(format:str) -> str
"""
import datetime

today = datetime.date.today()
print("12:",today)
print("13:",type(today))
today = datetime.datetime.today()
print("15:",today)
print("16:",type(today))
now = datetime.datetime.now()
print("18:",now)

# convert string to datetime
string1 = "1956-01-31" # format '%Y-%m-%d'
birthday = datetime.datetime.strptime(string1,'%Y-%m-%d')
print("23:",birthday)
print(type(birthday))
age = today.year-birthday.year
print(age)

# convert datetime to string
string2 = datetime.datetime.strftime(today, '%Y-%m-%d')
print(string2)

string2 = today.strftime('%Y-%m-%d')
print(string2)

year = today.strftime("%Y") 
print(f"year:  {year}")
month = today.strftime("%m") 
print(f"month: {month}")
day = today.strftime("%d") 
print("day:  ",day)
time = now.strftime("%H:%M:%S")
print("time: ", time)

print(birthday.strftime("%A, %B %d %Y"))

msg = "Guido was born on {:%A, %B %d %Y}."
print(msg.format(birthday))

moon_landing = "7/20/1969" # The date of first time man landing on the Moon
landing_date = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
msg = "First time man landing on the Moon on {:%A, %B %d %Y}."
print(msg.format(landing_date))
print(type(landing_date))