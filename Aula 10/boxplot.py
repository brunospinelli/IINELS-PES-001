import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(873842190)
all_data = [np.random.normal(0,std,size=100)for std in range(1,4)]
labels = ['x1','x2', 'x3']
fir, ax = plt.subplots(nrows=1,ncols=1,figsize=(9,4))

bplot = ax.boxplot(all_data,vert=True,patch_artist=True,labels=labels)

ax.set_title('Box Plot Retangular')
plt.show()