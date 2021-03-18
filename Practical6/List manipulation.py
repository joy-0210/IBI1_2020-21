#store the information
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]

#import module
import numpy as np
import matplotlib.pyplot as plt

a=np.array(gene_lengths)
b=np.array(exon_counts)
c=a/b #calculate the average exon length

plt.boxplot(c,
            showmeans=True, #Display average value
            patch_artist=True, #Enable custom color filling
            boxprops = {'color':'grey','facecolor':'beige'}, #Sets box fill color and border color
            meanprops = {'marker':'o','markerfacecolor':'yellow'}, #Set the shape and fill color of the mean point
            medianprops = {'linestyle':'--','color':'orange'})#Set the type and color of the median line
plt.title('exon length') #Set the name of the boxplot

plt.show()
