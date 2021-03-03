import matplotlib.pyplot as plt
import numpy as np

days = [1,2,3,4,5,6,7]
sales_1 = [120,230,434,345,344,454,123] # sales 1
sales_2 = [90,110,200,350,400,450,120] # sales 2
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
ypos = np.arange(len(sales_1))
plt.barh(ypos+0.1,sales_1,label = 'company 1',height = 0.5)
plt.barh(ypos-0.1,sales_2,label = 'company 2',height = 0.5)
plt.title('Sales per day\n in USD',color = 'Red',fontsize = 15)
plt.xlabel('sales',fontsize = 15,color = 'blue')
plt.ylabel('day of the week',fontsize = 15,color = 'blue')
plt.yticks(days,day_of_week)
plt.legend()
plt.show()