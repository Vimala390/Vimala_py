import pandas as pd 
x_d = {'day':['1/12/2020','13/12/2020','2/12/2020','10/12/2020'],'temperature':['20','30','40','50'],'windspeed':['23','3','12','13'],'event':['rain','sunny','snow','rain']
}

y = ['1/12/2020','13/12/2020','2/12/2020','10/12/2020']
df1 = pd.DataFrame(y)
df = pd.DataFrame(x_d)

print(df)
print(df.index)  # to print index
# to set the index
print(df.set_index('day',inplace= True)) # to set the day column as index

print(df)
print(df.loc['13/12/2020'])  # to locate the data of given value
df.reset_index(inplace=True) # To reset the inde it will return before index set data

print(df)
