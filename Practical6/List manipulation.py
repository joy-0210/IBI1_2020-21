import numpy as np
import matplotlib.pyplot as plt

#store the information
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]

#turn lists into arrays
lengths_array = np.array(gene_lengths)
counts_array = np.array(exon_counts)

#calculate the average exon length
average=lengths_array/counts_array

#sort and print the average length
sort=sorted(average)
print(sort)


plt.boxplot(sort,
            showmeans=True,                                             #Display average value
            patch_artist=True,                                          #Enable custom color filling
            boxprops = {'color':'grey','facecolor':'beige'},            #Sets box fill color and border color
            meanprops = {'marker':'o','markerfacecolor':'yellow'},      #Set the shape and fill color of the mean point
            medianprops = {'linestyle':'--','color':'orange'})          #Set the type and color of the median line
plt.title('exon length')                                                #Set the name of the boxplot

plt.show()
