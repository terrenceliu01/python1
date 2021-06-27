from datetime import date

def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))

print()
birthdate = input("Please enter your birth date(yyyy,mm,dd): ")
l = birthdate.split(',')
year = int(l[0])
month = int(l[1])
day = int(l[2])
age = calculate_age(date(year, month, day))
print(f"You are {age} years old.")
