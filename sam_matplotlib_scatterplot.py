import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
sales_1 = [120,230,434,345,344,454,123] # sales 1
sales_2 = [90,110,200,350,400,450,120] # sales 2

plt.scatter(days,sales_1,label = 'customer 1',color = 'red',s = 300,marker = '*')
plt.scatter(days,sales_2,label = 'customer 2',color = 'green',s = 300)
plt.title('sales per day\n in USD',fontsize = 17,color = 'orange')
plt.xlabel('Days',fontsize = 17,color= 'orange')
plt.ylabel('Sales',fontsize = 17,color= 'orange')
plt.legend()

plt.grid()
plt.show()