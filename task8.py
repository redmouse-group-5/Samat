import time
from datetime import datetime, timedelta, date

x = 19921105
print(datetime.strptime(str(x), '%Y%m%d'))

day = 5
month = 11
year = 1992
print(datetime.strptime(str(day)+str(month)+str(year), '%d%m%Y'))

st = '05/11/1992'
print(datetime.strptime(st, '%d/%m/%Y'))

today = datetime.today()
print(today)
a = today.replace(month=(today.month-1), year=(today.year+1))

print(a)
print(a.strftime('%j'))
print(a.timetuple().tm_yday)

n = 25
print (datetime(datetime.today().timetuple().tm_year, 1, 1) + timedelta(n - 1))

d = date.today()
print (d.strftime('%j'))

dt = str(input('Input a date in dd.mm.yyyy format: '))
dd = datetime.date(datetime.strptime(dt, '%d.%m.%Y'))
dm = time.strftime('%B %d %y', dd.timetuple())
print (dm)