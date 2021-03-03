import pandas as pd
##import xlrd 
print(pd.__version__)

df = pd.read_csv('C:/Users/Vimala_Revanuru/Desktop/sample_book.csv') ##,names=col_names,header=None)

print(df)
#print(df1)
x_d = {'day':['1/12/2020','13/12/2020','2/12/2020','10/12/2020'],'temperature':['20','30','40','50'],'windspeed':['23','3','12','13'],'event':['rain','sunny','snow','rain']
}

print(type(x_d))

df1 = pd.DataFrame(x_d)
print(df1)
print(df.shape)
r,c = df.shape
print(r,c)
print(df.head())  ## print first 5 rows 
print(df.head(1))
print(df.tail()) ## print last 5 rows 
print(df.tail(1))
print(df[2:4])
print(df1.columns) # to print columns
print(df.temperature) # df['temperature']

print(type(df))
print(type(df.temperature)) 

print(df[['day','temperature']])

print(df['temperature'].max())
print(df['windspeed'].sum())

print(df['windspeed'].mean()) ## Average
print(df.describe())  ## Statistics of data frame

## rows where temprature is maximum
print(df1[['day','temperature']][df1.temperature == df1.temperature.max()])