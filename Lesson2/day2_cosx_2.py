# calculate cos(x) from 0 to 2pi in 0.1 increments

import math as m

dx = 0.1
start = 0
stop = 2*m.pi
N = (stop - start) / dx

print('For Loop')
cos1 = []
for i in range(int(N)):
	value = m.cos(i*dx)
	cos1.append(value)
print(cos1)

# List comprehension
cos2 = [ m.cos(i*dx) for i in range(int(N)) ]
print('List Method')
print(cos2)

# While loop

cos3 = []
while start < stop:
	value = m.cos(start)
	cos3.append(value)
	start += dx
print('While Loop')
print(cos3)
