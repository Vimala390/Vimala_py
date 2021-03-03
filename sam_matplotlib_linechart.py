import matplotlib.pyplot as plt
days = [1,2,3,4,5,6,7] # time
sales_1 = [120,230,434,345,344,454,123] # sales 1
sales_2 = [90,110,200,350,400,450,120] # sales 2

plt.figure(figsize = (7,5))
plt.plot(days,sales_1,marker = 'o',markersize = 15,color = 'Red',linestyle = '--',label = 'Company 1')  # Line related
plt.plot(days,sales_2,marker = '*',markersize = 15,color = 'green',linestyle = '-',label = 'Company 2') #
#plt.plot(days,sales_1,'ro--',markersize = 15)
plt.grid(color = 'Yellow')
#plt.fill_between(days,sales_1,color = 'orange',alpha = 0.3)
plt.ylim(50,470)
#plt.yticks([100,200,300,400,500])
plt.title('Sales per day\n in EUR',fontsize = 10,color = 'Green') # Title related
plt.xlabel('Day of the week',fontsize = 10,color = 'Blue') # x axis relaed
plt.ylabel('Sales_1',fontsize = 10,color = 'Red') # Y axis related
plt.axhline(250,linewidth = 3,color = 'black',label = 'Target sales') # Horizontal line - Target sales of companies
plt.legend(loc = 'lower center',fontsize = 15) # to differentiate plots by showing labels of plot

plt.show()

