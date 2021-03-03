import matplotlib.pyplot as plt

expenses = ['Food','Rent','Books','Sports','Other']
values = [500,450,200,300,550]

plt.pie(values, labels = expenses,autopct = '% 0.2f%%',explode = [0.05,0.05,0.05,0.05,0.05])
#To make pie chart as Doughnut chart add below pie chart
plt.pie([1,1], labels = None,radius = 0.5,colors = ['white','white'],explode = [-0.005,-0.005])
plt.title('Overview of expenses',fontsize = 20,color = 'Red')

plt.show()