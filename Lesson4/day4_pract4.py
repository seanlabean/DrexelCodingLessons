#Creat an array between 0 and 100 with N*M steps
##Convert this into an NxM matrix

import numpy as np

N = int(input('What is N?: '))
M = int(input('What is M?: '))

My_ar = np.linspace(0,100,N*M)
mat = np.reshape(My_ar, (N,M))

print(mat)
