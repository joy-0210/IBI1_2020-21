import numpy as np
import matplotlib.pyplot as plt

#create a dictionary to store data and print it
coutry={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
print (coutry)

#turn the values and lables into array so that the frequency table will still match the input when the input table is changed
values = np.array([i for i in coutry.values()])
labels = np.array([j for j in coutry.keys()])

#Draw the pie chart
explode=[0.1,0.1,0.1,0.1,0.1] #Set each item n radii from the center of the circle
colors=['beige', 'indigo','blue', 'cyan','yellow'] #set colors for each item
plt.pie(values,labels=labels,explode=explode,colors=colors,shadow=True,autopct='%1.1f%%') #Draw the pie chart
plt.title('COVID-19')
plt.show()
