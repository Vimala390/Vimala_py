import matplotlib.pyplot as plt

no_of_hours = [4,5,7,8,9,10,12,14,15,17,18,19,21,23,24]

plt.hist(no_of_hours,label = 'no_of_hours',color = 'blue',rwidth = 0.9,edgecolor = 'red',bins = [4,8,12,16,24])
plt.title('distribution of study hours',fontsize = 18,color='orange')
plt.xlabel('No of hours',fontsize = 18,color = 'orange')
plt.ylabel('No of students',fontsize = 18,color = 'orange')
plt.yticks([1,2,3,4,5])
plt.legend()
plt.show()