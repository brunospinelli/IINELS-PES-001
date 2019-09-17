import numpy as np 
a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11]])
b = np.array([1,2])
c = np.array([0,2])

print (a[[False, True, True],[True, False, True,False]])

print (a[[False, True, True],:])

print(a[b,c])