import numpy as np 

pallete = np.array([[0,0,0
],
                    [255,0,0],
                    [0,255,0],
                    [0,0,255],
                    [255,255,255]])

image = np.array([[0,1,2,0],
                    [0,3,4,0]])

print(pallete[image])