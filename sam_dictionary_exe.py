#Write a program to convert a string into key-value pairs and store them into 
# a dictionary.
#Example: str="Johan=123,wick=234,philip=500,peter=900"
import re
str1 = 'Johan=123,Wick=234,Philip=500,Peter=900'
name1 = re.findall('[A-Z][a-z]+',str1)
val1 = re.findall('[0-9]+',str1)
print(name1)
print(val1)
dict1 = {}
x = 0
for i in name1:
    dict1[i] = val1[x]
    x+=1

print(dict1)