import datetime

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
m, d = (int(x) for x in input().split())
print(days[datetime.datetime(2009, d, m).weekday()])
