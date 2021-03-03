#1) Please explain the reason for having the followign code result as False and how this can be modified to get the result as "true"
a=4.2
b=2.1
c = a+b;print(type(a))
print(type(b))
print(type(c))
if (a+b==6.3):
    print('True')
else:
    print('False')


#2) How to pick random number from a sequence?
import random as rn
lst = [1,2,3,4,5,'six','seven',8,9]
print('Random number from list',rn.choice(lst))



#3) Write a program to display the number of days between two dates
from datetime import datetime

datetime_object1 = datetime.strptime('OCT 1 2020  1:33PM', '%b %d %Y %I:%M%p')

datetime_object2 = datetime.strptime('OCT 10 2020  1:33PM', '%b %d %Y %I:%M%p')
print(datetime_object2 - datetime_object1)

#4) How to convert a string into datetime?
from datetime import datetime
date_str = '17/10/20 01:55:19'
print(type(date_str))
date_str_date = datetime.strptime(date_str,'%d/%m/%y %H:%M:%S')
print(date_str_date)
print(type(date_str_date))

#5) You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. At
#what local time did your friend in Bangalore, India, have to show up to attend?

