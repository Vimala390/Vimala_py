stg1 = 'good'
stg2 = 'morning'
stg4 = 'Hey';stg5 = 'Vimala'
stg3 = stg1+" " +stg2
print(stg3)
print('{} {}!! {} {}...'.format(stg4,stg5,stg1,stg2))
str6 = '    Vimala    '
print(str6.lstrip())
print(str6.rstrip())
print(str6.strip())

# Reverse Each word in the string [Eg. Have a great day  O/p - evaH a taerg yad]
str_1 = 'Vimala welcome' ##input('enter string ..')   ##'Vimala welcome'
str_1 = str_1+" "
tmp = ''
rev = ''
for i in str_1:
    if i!= " ":
        tmp = i+tmp
    else:
        rev = rev+" "+tmp
        tmp = ""
        #continue
print(rev)

##Efficient way
import re 
x = 'Have a great day'
x_1 = x.split()  ###
x_2 = re.findall('[a-zA-Z]*\s+',x)
print(x.split())
print(x_2)
for i in x_1:
    print(i[::-1],end =" ")


s = "HELLO there HOW are YOU"
#print(re.findall("(?<!^)\s+(?=[A-Z])(?!.\s)",s))
l = re.compile("(?<!^)\s+(?=[A-Z])(?!.\s)").split(s)
print(l)

stg = "asdf fjdk; afed, fjek,asdf, foo"
s1 = re.compile("(?<!^)\s+(?=[a-z])(?!.\s)").split(stg)
#s1_1 = re.findall('[a-z]*\s+',stg)
print(stg.split())
print(re.split(';,',stg))







