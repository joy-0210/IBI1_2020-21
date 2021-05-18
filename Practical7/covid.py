import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# change the working directory to where the "full_data.csv" file is stored
os.chdir("/Users/jinxt/Downloads")

# check that what I have done is correct
os.getcwd() 
os.listdir()

#use the pandas library to read the content of the .csv file into a dataframe object
covid_data=pd.read_csv("full_data.csv")

#show all columns, and every second row between (and including) 0 and 10
print("all columns, and every second row between 0 and 10 :")
print(covid_data.iloc[0:11:2,:])

#select the row where location is Afghanistan
L1=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Afghanistan":
		L1.append(True)
	else:
		L1.append(False)
# show all cases in Afghanistan
print("all cases in Afghanistan:")
print(covid_data.loc[L1,"total_cases"] ) 

#select the row for the world
L2=[]
for i in range (0,7996):
     if covid_data.iloc[i,1]=="World":
             L2.append(True)
     else:
             L2.append(False)
             
#store the data for world and calculate    
world_dates=covid_data.loc[L2,"date"]
world_new_deaths=covid_data.loc[L2,"new_deaths"] 
world_new_cases=world_new_cases=covid_data.loc[L2,"new_cases"]

#Use numpy to compute both the mean and the median for new cases around the world
print("mean: "+str(np.mean(world_new_cases))) 
print("median: "+str(np.median(world_new_cases)))

#make a boxplot for World_new_case
plt.boxplot(world_new_cases,
            showmeans=True, 
            patch_artist=True,
            boxprops = {'color':'grey','facecolor':'beige'}, 
            meanprops = {'marker':'o','markerfacecolor':'yellow'}, 
            medianprops = {'linestyle':'--','color':'orange'})
plt.xlabel('dates')
plt.ylabel('new cases')
plt.title('worldwide situation')
plt.show()

#plot both new cases and new deaths worldwide in the graph
plt.plot(world_dates, world_new_cases, 'bo', label='new cases')
plt.plot(world_dates, world_new_deaths, 'r+', label='new deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('world dates')
plt.ylabel('human number')
plt.title('new cases and new deaths for the entire world')
plt.legend()
plt.show()


#answer the question.txt

# select the data in Spain
L3=[]
for i in range (0,7996) :
     if covid_data.iloc[i,1]=="Spain" :
             L3.append(True)
     else:
             L3.append(False)
print("new cases and total cases in Spain")
print(covid_data.loc[L3,"new_cases"])
print(covid_data.loc[L3,"total_cases"] )

#store the data
Spain_new_cases=covid_data.loc[L3,"new_cases"]
Spain_total_cases=covid_data.loc[L3,"total_cases"]
Spain_date=covid_data.loc[L3,"date"]
#plot both new cases and total cases for Spain in the graph
plt.plot(Spain_date,Spain_new_cases,"b-", label='new cases')
plt.plot(Spain_date,Spain_total_cases,"r-", label='total cases')
plt.xticks('date')
plt.ylabel('human number')
plt.title('new cases and total cases in Spain')
plt.yticks(np.arange(0,80001,5000))
plt.xticks(Spain_date.iloc[0:len(Spain_date):4],rotation=-90)
plt.legend()
plt.show()
