#Create an array of cos(x) and a second array of sin(x), incremented by 0.1
#Use these to create a third array of cos(x)**2 + sin(x)**2

import numpy as np

X = np.arange(0, 2.0*np.pi, 0.1)

ANS = np.sin(X)**2 + np.cos(X)**2


print(np.sin(X))
print(np.cos(X))
print(ANS)
 
 
