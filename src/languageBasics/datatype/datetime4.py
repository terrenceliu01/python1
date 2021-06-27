"""
datatime, date, time
Reused first stage rocket: March 30, 2017 22:27 UTC
"""

import datetime

launchdate = datetime.date(2017, 3, 30)
launchtime = datetime.time(22,27,0)
launchdatetime = datetime.datetime(2017, 3, 30,22,27,0)

print(launchdate) # only date
print(launchtime) # only time
print(launchdatetime) # date and time

print(launchdate.year)
print(launchdate.month)
print(launchdate.day)

print(launchtime.hour)
print(launchtime.minute)
print(launchtime.second)

print(launchdatetime.year)
print(launchdatetime.month)
print(launchdatetime.day)
print(launchdatetime.hour)
print(launchdatetime.minute)
print(launchdatetime.second)
