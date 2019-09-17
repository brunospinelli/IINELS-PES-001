import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

t = np.arange(0.0, 5.0, 0.01)

fig,ax = plt.subplots(2,2)

ax [0,0].plot(np.sin(2* np.pi * t) * np.exp(-0.5 * t))
ax [0,0].set_title("Vibração atenuada", fontsize=10)

ax [0,1].plot(np.sin(2* np.pi * t) * -(np.log(0.5 * t)))
ax [0,1].set_title("Vibração logada", fontsize=10)

ax [1,0].plot(np.sin(2* np.pi * t) * np.cos(180 * t))
ax [1,0].set_title("Vibração cossenada", fontsize=10)

ax [1,1].plot(np.sin(2* np.pi * t) * np.tan(45* t))
ax [1,1].set_title("Vibração tangentada", fontsize=10)

plt.show()