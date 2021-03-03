from datetime import datetime
import re
date_1 = '11/27/2020'
date_1_form = datetime.strptime(date_1,'%m/%d/%Y').strftime('%Y-%m-%d')
#print(date_1_form)
date1 = re.compile('\d{2}/\d{2}/\d{4}')
date_1 = date1.sub(date_1_form,date_1)

print(date_1)

#import string 
str1 = 'asdf fjdk; afed, fjek,asdf, foo'
str1_f = re.split('[;,\s]\s*',str1)
print(str1_f)
#print(str1.split())
from operator import *
if le(4,2):
    print('yes')
else:
    print('No')