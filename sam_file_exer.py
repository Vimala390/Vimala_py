#Python supports Binary(other than Text files i.e. images ..etc) and Text files
# Syntax :- Open(filename,Mode)
# default mode -  'r'  -- open file for reading , Error if file doesnot exists
#                  'a' - Append -- open file for appending, creates file if does not exists.
#                  'w' - write - open file for writing ,if exists it will overwrite. create the file if doe not exists
#                  'x' - create - create the specified file. returns error if file exists.

#import os
file = open ('C:/Users/Vimala_Revanuru/Desktop/new 1.txt','r')
print(file.read(5))
file.close()

file = open('C:/Users/Vimala_Revanuru/Desktop/sam_demo.txt','a')
#print(file.read())
file.close

file = open('C:/Users/Vimala_Revanuru/Desktop/sam_demo.txt','r')
#print(file.readline())
file.close

## To print all lines using for loop
file = open('C:/Users/Vimala_Revanuru/Desktop/sam_demo.txt','r')
for line in file:
    print(file.read())

file.close

file = open('C:/Users/Vimala_Revanuru/Desktop/sam_demo_1.txt','w')
file.write('Welcome to demo_1')
file.write('\n')
file.write('It is for demo purpose only ...')
#print(file.readlines())

file = open('C:/Users/Vimala_Revanuru/Desktop/sam_demo_1.txt','r')
for line in file:
    print(file.readline())

file.close

# Removing/delete file and Directory 
from os import *
#remove('C:/Users/Vimala_Revanuru/Desktop/demo/sam_demo_1.txt')
if path.exists('C:/Users/Vimala_Revanuru/Desktop/demo/sam_demo_1.txt'):
    remove('C:/Users/Vimala_Revanuru/Desktop/demo/sam_demo_1.txt')
else:
    print('file not exists')

#remove('C:/Users/Vimala_Revanuru/Desktop/demo/sam_demo.txt')
#rmdir('C:/Users/Vimala_Revanuru/Desktop/demo') ## Remove directory

#Pickle -- convert structure format/readable format to Binary format
# Pickle.dump(<structure>,filename) -- to write into file
#Pickle.load(fileobject) -- to read the data from file
#Unpickle -- Convert Binary format to structure format/readable format

