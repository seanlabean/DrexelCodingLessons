
import numpy as np
from numpy import linalg

A = [[2,0,4], [0, 1, 0], [0, 3, 9]]

eVals, eVecs = linalg.eig(A)
print(eVals, eVecs)


eVecs = np.mat(eVecs)
AA = np.mat(A)


print(eVecs.I * AA * eVecs)
