import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

eating = [2,1,3,2,2,2,2]
sleeping = [7,7,8,5,7,5,8,]
reading = [1,2,2,3,1,1,2]
playing = [2,2,1,3,2,1,4]

print(plt.style.available)
plt.style.use('dark_background')
plt.stackplot(days,eating,sleeping,reading,playing,labels = ['eating','sleeping','reading','playing'])
plt.title('Activities in a week',fontsize = 18,color = 'red')
plt.ylabel('Activities',fontsize =18,color = 'red')
plt.xlabel('Day of the week',fontsize =18,color = 'Red')
plt.yticks([1,4,8,12])
plt.legend(loc = 'upper left')
plt.savefig('Activities_in_week.png')  # to save figure
plt.show()