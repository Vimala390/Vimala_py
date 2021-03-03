#Handling Missing data in python 
#1. fillna to fill missing values using different ways
import pandas as pd 
#def con_temperature(temp):
 #   if temp == Null:

# convert day column as DATE type . Usually when it reads from file it will be string in csv file
df = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\weather_data_c.csv',parse_dates=["day"])
#print(type(df.day[0]))
#print(df)
#in excel file we do need to convert while reading it self it will read as timestamp
#df = pd.read_excel('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\weather_data.xls')
# use day as index column
df.set_index('day',inplace = True)
#print(df)
########### Fillna################
# to replace values with meaning full data

new_df = df.fillna({'temperature':0,'windspeed':0,'event':'no event'})
#print(new_df)
######## to carry froward the previous day data/fill 0 values with previous day data ##############
new_df1 = df.fillna(method = 'ffill')
#print(new_df1)

######to carry froward the next day data/fill 0 values with next day data ###############
new_df2 = df.fillna(method = 'bfill')
#print(new_df2)
###################################################################################
## to carry froward the previous day data and copy only once
###################################################################
new_df4= df.fillna(method = 'ffill',limit = 2)
print(new_df4)

#2. interpolate to make a guess on missing values using interpolation
df_1 = pd.read_csv('C:\\Users\\Vimala_Revanuru\\Desktop\\py_pandas\\weather_data_c.csv')
print('***********interpolate*****************')
df_1.set_index('day',inplace = True)
print(df_1)
df_2 = df_1.interpolate(method = "linear")
print(df_2)
#3. dropna to drop rows with missing values
print('**************** dropna ********************')
print(df_1.dropna())  ## will drop row if atleast one column is Null
## drop row if all columns have null data
print(df_1.dropna(how = 'all'))
print(df_1.dropna(thresh = 2))
