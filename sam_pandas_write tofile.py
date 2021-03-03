######################################################
# Reading and writing CSV,excel files
#######################################################
# 1. Read CSV
import pandas as pd 
df = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data.csv')
print(df) 
### Skip Header/Extra header in csv file
df1 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data.csv',skiprows=1)
## (OR) use header = 1 means -- header will start from 1
df2 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data1.csv',header=1)
print(df1)
print(df2)
## Provide header names to file which does not have header/Missing Header
df3 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data3.csv',header=None,names=["tickers","eps","revenue","price","people"])
print('********Provide header names to file which does not have header*******')
print(df3)
##read 3 rows from file
df4 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data.csv',nrows=3)
#print(df4.head(3)) #including header
print(df4)
## Cleanup messy data  from file
df5 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data.csv',na_values=['not available','n.a.'])
print("Cleanup messy data **********")
print(df5)
## Supply dictionary for replace with "na_values"
df6 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data.csv',na_values= {"eps":['not available','n.a.'],"price":['not available','n.a.',0],"revenue":['not available','n.a.',-1]})
print("Supply dictionary for replace with : ""na_values""")
print(df6)
####################################################################
#2. Write CSV
####################################################################
print('\n')
print("writing  dataframe to csv file .....")
print('\n')
df6.to_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\new_write.csv',index=False) # To skip the index value
# Skipping columns to while writing to file
df6.to_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\new_write1.csv',index=False,header=False,columns=["tickers","eps"])
print("Skipping columns to while writing to file")
#print(df7)
#################################################################
#3. Read excel
##################################################################
print("*******************Read excel file **************")
def convert_people(people):
    if people == 'n.a.':
        return 'Veera'
    return people
def convert_eps(eps):
    if eps == 'not available':
        return 0
    return eps

df_ex = pd.read_excel('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data_x.xls',
                        na_values=['not available','n.a.'],
                        converters= { 'people':convert_people,'eps':convert_eps}
                        )
print(df_ex)
##########################################
#4. write to excel
##########################################
print('******************write to excel file**************************')
df_ex.to_excel('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data_x_write.xls',sheet_name = "Sheet1",index = False,
                startrow = 2,startcol = 2)
####################################################################################
# Write two dataframes into same excel file in two different sheets using ExcelWriter
#####################################################################################
x_d = {'day':['1/12/2020','13/12/2020','2/12/2020','10/12/2020'],'temperature':['20','30','40','50'],'windspeed':['23','3','12','13'],'event':['rain','sunny','snow','rain']
}
df_2 = pd.DataFrame(x_d)
print(df_2)

y_d = [('1/12/2020','20','rain'),('12/12/2020','21','sunny'),('13/12/2020','25','rain')]
df_3 = pd.DataFrame(y_d,columns=["day","temperature","event"])
print(df_3)

with pd.ExcelWriter('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\stock_data_writer.xls') as wr:
    df_2.to_excel(wr,sheet_name = 'weather',index = False)
    df_3.to_excel(wr,sheet_name = 'weather_report',index = False)