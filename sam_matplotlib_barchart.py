import matplotlib.pyplot as plt
import numpy as np 
days = [1,2,3,4,5,6,7] # days
sales_1 = [120,230,434,345,344,454,123] # sales 1
sales_2 = [90,110,200,350,400,450,120] # sales 2


day_of_week = ['Mon','Tue','Wed','thu','Fri','sat','sun']
x_pos = np.arange(len(days))

plt.figure(figsize = (7,5))
#plt.bar(days,sales_1,label = 'Company 1',color = 'blue',width = 0.5)
plt.bar(x_pos+0.1,sales_1,label = 'Company 1',color = 'blue',width = 0.5)
plt.bar(x_pos-0.1,sales_2,label = 'Company 2',color = 'orange',width = 0.5)
#plt.bar(days,sales_2,label = 'Company 2',color = 'orange',width = 0.5)
plt.title('Sales per day\n in USD',color = 'blue',fontsize = 15)
plt.xlabel('Day of the week',color = 'blue',fontsize = 15)
plt.ylabel('Sales',color = 'blue',fontsize = 15)
plt.xticks(x_pos,day_of_week)
plt.legend(loc = 'upper left')
#plt.axhline(250,color = 'green')
#plt.grid()
plt.show()