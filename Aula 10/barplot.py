import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

N = 5
mediaHomens = (20,35,30,35,27)
mediaMulheres = (25,32,34,36,17)
desvpadHomens = (2,4,3,4,1)
desvpadMulheres = (2,3,5,2,1)

ind = np.arange(N)
width = 0.35

p1 = plt.bar(ind,mediaHomens, width, yerr = desvpadHomens)
p2 = plt.bar(ind, mediaMulheres, width, yerr = desvpadMulheres)

plt.ylabel('Porutação')
plt.title('Pontuação por grupo e gênero')
plt.xticks(ind,('G1','G2', 'G3','G4','G5'))
plt.yticks(np.arange(90,81,10))
plt.legend((p1[0],p2[0]),('Homens', 'Mulheres'))

plt.show()