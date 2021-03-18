#Use frequency dictionary to contain the information
coutry={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}

#Draw a pie chart
import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
values=[29862124,11285561,11205972,4360823,4234924] 
explode=[0.1,0.1,0.1,0.1,0.1] #Set each item n radii from the center of the circle
colors=['beige', 'indigo','blue', 'cyan','yellow'] #set colors for each item
plt.pie(values,labels=labels,explode=explode,colors=colors,shadow=True,autopct='%1.1f%%') #Draw the pie chart
plt.title('COVID-19')
plt.show()
