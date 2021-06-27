"""
calculate date by day interval
"""
import datetime

begin2000 = datetime.date(2000, 1, 1)
# what is the date after 100 days?
delta = datetime.timedelta(days=100) # default is days
after100 = begin2000 + delta
print(after100)

today = datetime.datetime.today()
# what is the time after 100 hours? (plan to do something in 100 hours, figure out exactly date and time)
delta = datetime.timedelta(hours=100)
after100hours = today + delta
print(after100hours)

delta = datetime.timedelta(weeks=16)
pythonBegin = datetime.date(2021,4,18)
print(f"Python one-on-one start at: {pythonBegin}")
pythonEnd = pythonBegin + delta
print(f"one-on-one end at: {pythonEnd}")


pythonBegin = datetime.date(2021,1,19)
print(f"Python weekend class start at {pythonBegin}")
today = datetime.date.today()
print(f"today is {today}")
diff = today - pythonBegin
print(diff.days, " days passed.")
print(int(diff.days/7) + 1, " weeks passed.")