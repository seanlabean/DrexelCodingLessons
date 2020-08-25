#Write a function that takes in two vectors and prints whether they are parallel, perp, or neither.
## Assume 3D arrays.

import numpy as np

print('I need two 3D vectors, please')
print('What is the first vector?: ')

x,y = [],[]
for i in range(0,3):
	x.append(float(input()))

print('What is the second vector?: ')
for i in range(0,3):
	y.append(float(input()))


comp_c = np.cross(x,y)
comp_d = np.dot(x,y)

if not comp_c.any():
	out = 'Parallel'
elif comp_d == 0:
	out = 'Perpendicular'
else:
	out = 'neither'

print('The two vectors are %s'  % (out))
