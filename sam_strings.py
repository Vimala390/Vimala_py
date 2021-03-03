str1 = "Vimala's laptop"
print(str1)
print('vimala\'s laptop')
str2 = """ Hey Vimala
        welcome to python3"""

print(str2)
print(len(str1))
print(str1[0:len(str1)])
print(str1[::-1]) ##Reverse string 
print(str1.upper()) #Upper case
print(str1.lower()) #lower case
print(str1.index('l',0,15))
print(str1.find('l',0,10))
print(str1.count('l',5,10)) # No. of occurences
x = str1.split(" ")  ###Return List 
y = tuple(str1.split(" ")) ## cascade with tuple
z = str1.rpartition("'s")  ##partition using seperator
print('Z is ',z)
print(y)
print(x)
print(type(x))
print(type(y))
print(type(z))
print(str1.replace('Vimala','Veera'))
import string as s
print(s.capwords(str1,sep = None)) # split and capitalize each word first letter
print(s.capwords('Python is one of the best programming languages',sep = None))

import re
st1 = 'Python 123'
regst = re.compile('')
st1_new = regst.sub('',st1)
print(st1_new)
#rewrite dates of the form “11/27/2012” as “2012-11-27.”

