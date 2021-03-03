#Different ways of creating Data Frame
#1. Using CSV
import pandas as pd 
df = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\sample_data.csv')
print(df)
#2.using Excel 
#the latest version of xlrd (2.0.1) only support .xls files.
#so this error can be solved by installing an older version of xlrd.
#use commands below in cmd:
###############################
#pip uninstall xlrd
#pip install xlrd==1.2.0  --  will support .xlsx format
################################
df1 = pd.read_excel("C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\sample_book.xls","Sheet1")
print(df1)
#3.From python dictionary
x_d = {'day':['1/12/2020','13/12/2020','2/12/2020','10/12/2020'],'temperature':['20','30','40','50'],'windspeed':['23','3','12','13'],'event':['rain','sunny','snow','rain']
}
df2 = pd.DataFrame(x_d)
print(df2)

#4.From list of tuples
print('From list of tuples')
y_d = [('1/12/2020','20','rain'),('12/12/2020','21','sunny'),('13/12/2020','25','rain')]
df3 = pd.DataFrame(y_d,columns=["day","temperature","event"])
print(df3)
#5.From list of dictionaries
z_d = [{'day':'1/12/2020','temperature':'20','event':'rain'},
{'day':'12/12/2020','temperature':'21','event':'sunny'},
{'day':'13/12/2020','temperature':'25','event':'rain'}]

df4 = pd.DataFrame(z_d)
print(df4)