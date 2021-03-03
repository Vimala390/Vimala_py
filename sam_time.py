import time as dt

print(dt.time())
a = dt.localtime()
print(a)
print(dt.ctime())
print(dt.asctime(a))
#print(dt.strftime('Sat Oct 17 2020 06:49:17','%m/%d/%y'))


import datetime as dt
from datetime import datetime, timezone
print(dt.datetime.now())
v = dt.datetime.now()
print(v.year)
print(v.month)
#print(tzname())
a1 = dt.timedelta(days=10)
a2 = dt.timedelta(days=5)
b = a1-a2;print(b)

from datetime import datetime

datetime_object1 = datetime.strptime('OCT 1 2020  1:33PM', '%b %d %Y %I:%M%p')

datetime_object2 = datetime.strptime('OCT 10 2020  1:33PM', '%b %d %Y %I:%M%p')
print(datetime_object2 - datetime_object1)

from datetime import datetime
date_str = '17/10/20 01:55:19'
print(type(date_str))
date_str_date = datetime.strptime(date_str,'%d/%m/%y %H:%M:%S')
print(date_str_date)
#print(type(date_str_date))
date_1 = '11/27/12'
date_1_form = datetime.strptime(date_1,'%m/%d/%y')
date_1_strf = datetime.strftime(date_1_form,'%Y-%m-%d')
print(date_1_strf)
#print(date_1_form)



