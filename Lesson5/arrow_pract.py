#quick illustration of day4_pract3.py

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [int(x) for x in input('x: ').split()]
y = [int(x) for x in input('y: ').split()]

comp_c = np.cross(x,y)
comp_d = np.dot(x,y)

vecs = [x,y,comp_c]
ls = ['x','y','cross']

if not comp_c.any():
	out = 'Parallel!'
elif comp_d == 0:
	out = 'Perpendicular'
else:
	out = 'neither'

print('The vectors are %s' % (out))

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
i = 0
c = ['r','b','g','k']
for _ in vecs:
#	print(_)
	ax.plot([0,_[0]],[0,_[1]],[0,_[2]],lw=3,color=c[i],label=ls[i])
	i+=1
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend(loc='best')
plt.show()
