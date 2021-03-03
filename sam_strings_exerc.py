#1) Reverse the string using for loop by using the slicing options
# (i.e. [start: stop: stepsize].  Here is the example using while loop. 
str1 = "Vimala's laptop"
print(str1[0:len(str1)])
print(str1[::-1]) ##Reverse string 


#2) rstrip(), lstrip() and strip() used to remove the spaces on left, right and both 
# sides of a string accordingly.
x = input('Enter input string ..')
print('Length of string before:',len(x))
x_1= x.strip()
print('Length of string after :' ,len(x_1))
y = input('Enter input string ..')
print('Length of string before:',len(y))
y_1= y.lstrip()
print('Length of string after :' ,len(y_1))
z = input('Enter input string ..')
print('Length of string before:',len(z))
z_1= z.rstrip()
print('Length of string after :' ,len(z_1))


#3) You need to split a string into fields, but the delimiters (and spacing around them) aren’t
#consistent throughout the string.  Example: line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
str1 = 'asdf fjdk; afed, fjek,asdf, foo'
str1_f = re.split('[;,\s]\s*',str1)
print(str1_f)
#4) Use the sub() functions/methods in the re module. To illustrate, 
# suppose you want to rewrite dates of the form “11/27/2012” as “2012-11-27.”
from datetime import datetime
import re
date_1 = '11/27/2020'
date_1_form = datetime.strptime(date_1,'%m/%d/%Y').strftime('%Y-%m-%d')
#print(date_1_form)
date1 = re.compile('\d{2}/\d{2}/\d{4}')
date_1 = date1.sub(date_1_form,date_1)

print(date_1)

#5) Use the sub() functions/methods in the re module. To illustrate, 
# suppose you want to rewrite dates of the form “11/27/2012” as “2012-11-27.”
