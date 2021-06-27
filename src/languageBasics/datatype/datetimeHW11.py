import datetime
today = datetime.date.today()
print("current date:", today)
year,week_num,day_of_week = today.isocalendar() # DOW = day of week
print()
print("Year %d, Week Number %d, Day of the Week %d" %(year,week_num, day_of_week))
print()
