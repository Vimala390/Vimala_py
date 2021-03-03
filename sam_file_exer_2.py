file = open('C:/Users/Vimala_Revanuru/Desktop/sam_demo_1.txt','r')
x = 'deno'
for line in file:
    if x in line:
        print('word found ..')
    else:
        print('Not Found ..')
