# Write a program to count number of lines, words and characters in a text file.
file = 'C:/Users/Vimala_Revanuru/Desktop/sam_demo_1.txt'
c_lines = 0
c_words = 0
c_chars = 0

for lines in open(file,'r'):
    c_lines+=1    
    print(lines.split())
    #print(len(lines))
    
    for char in lines:
        if char != ' ':
            c_chars+=1
    else:        
        pass
    for words in lines.split():
        c_words+=1


print('No.of Lines :' , c_lines)
print('No.of Characters:',c_chars)
print('No.of words:',c_words)

# Pickle

#Pickle -- convert structure format/readable format to Binary format
# Pickle.dump(<structure>,filename) -- to write into file
#Pickle.load(fileobject) -- to read the data from file
#Unpickle -- Convert Binary format to structure format/readable format

import pickle

def binary_write():
    file = open('C:/Users/Vimala_Revanuru/Desktop/Binary_data.dat','wb')
    list1 = ['vimala','Manoj','Veera','Tejansh']
    pickle.dump(list1,file)
    file.close()

def binary_load():
    file = open('C:/Users/Vimala_Revanuru/Desktop/Binary_data.dat','rb')
    lst = pickle.load(file)
    file.close()
    print(lst)
    

binary_write()
binary_load()



