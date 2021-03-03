import re
text = "John is 22 and Baby is 23 Veera is 15 and Teja is 24"
name1 = re.findall('[A-Z][a-z]*',text)
age = re.findall('[0-9]{2}',text)
print(name1)
print(age)
x = 0 
agedict = {}
for i in name1:
    agedict[i] = age[x]
    x+=1

print(agedict)
x_1 = re.findall('x1','fsdsgdjhghdx1dgfjhdgfx1')
print(x_1)
if re.findall('x1','fsdsgdjhghdx1dgfjhdgfx1'):
    print('true..')

for i in re.finditer('x1','fsdsgdjhghdx1dgfjhdgfx1'):
    print(i.span())

#Pattern
x = 'sat,hat,mat,cat'
alls = re.findall("[shmc]at",x)
print(alls)
y = 'sit,Kit,pit,tit,12it'
als = re.findall('[sKpt12]it',y)
s_1 = re.findall("[0-9]{2}it",y)
print(s_1)
print(als)

####################################
##  Replace word  ###################
fd = "hit kit pit lit tit"
r1 = re.compile("[l]it")
fd = r1.sub("cat",fd)
print(fd)
s1 = "here is \\\drop"
print(r"here is \\\drop")
print(s1)
### Replace new lines with space
import re
x = '''Hi Aspirant 
       welcome to python world
       Hello World !!!'''

print(x)
x_new = re.compile('\f')
x = x_new.sub("",x)
print(x)

p = "12 123 1234 12345 123456"
p1 = re.findall("\d{2}",p)
print(p1)
# phone number validation
#'\w' = [a-zA-z0-9_]
#'\W' = [^a-zA-z0-9]
phn = '234-345-2343'
#phn = p_new.sub('-',p_new)
print(phn)
if re.search('\w{3}-\w{3}-\w{4}',phn):
    print('Phone num is valid..')
else:
    print('Phone num is invalid')
##print()
# Name validation
#'\s' = [\f\n\r\t\v]
#'\S' = [^\f\n\r\t\v]

if re.search('\w{2,20}\s\w{2,20}','Vimala Revanuru'):
    print('name is valid')
else:
    print('name is invalid')
