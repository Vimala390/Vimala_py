class student:
    perc_rise = 1.05
    def __init__(self,first,last,marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + last+'@school.com'
    
    def fullname(self):
        return 'fullname is : {} {}'.format(self.first,self.last)
    
    def apply_rise(self):
        self.marks=int(self.marks*perc_rise)


std_1 = student('vimala','R',89)
std_2 = student('veera','I',99)

print(std_1.email)
print(std_2.email)
print(std_1.fullname())
print(std_2.fullname())
print(std_1.__dict__)
print(std_2.__dict__)

class dumb(student):
    perc_rise =1.10
    def __init__(self,first,last,marks,pro_lang):
        super().__init__(first,last,marks)
        self.pro_lang = pro_lang

std_1=dumb('Vimala','R',89,'Python')
print(std_1.marks)
#std_1.apply_rise()
print(std_1.perc_rise)
print(std_1.pro_lang)

#print(help(dumb))
