import time
from datetime import datetime, date

x = time.strptime('2015 50 1', '%Y %W %w')
print(type(x))
print(x)
print(time.asctime(x))

birthDate = datetime(1982,11,12)
timeTuple = birthDate.timetuple()
print(timeTuple)
print(time.asctime(timeTuple))
