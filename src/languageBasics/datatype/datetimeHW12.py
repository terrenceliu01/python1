import calendar

year = int(input("Please enter a year: "))
# Show every month
for month in range(1, 13):
    cal = calendar.monthcalendar(year, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]

    # If a Saturday presents in the first week, the second Saturday
    # is in the second week.  Otherwise, the second Saturday must 
    # be in the third week.
    
    if first_week[calendar.SATURDAY]:
        holi_day = second_week[calendar.SATURDAY]
    else:
        holi_day = third_week[calendar.SATURDAY]

    print('%s: %s' % (calendar.month_abbr[month], str(holi_day).zfill(2)))
	