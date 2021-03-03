import seaborn as sn
import matplotlib.pyplot as plt

fmri = sn.load_dataset('fmri')
#print(fmri.head())
#print(sn.__version__)
#print(sn.get_dataset_names()) # predefined data sets
tip = sn.load_dataset('tips')
print(tip.head())
#sn.lineplot(x = 'smoker',y = 'sex', data = 'tip')
sn.barplot(x = 'day',y = 'total_bill',data = tip,hue= 'sex')
plt.show()
