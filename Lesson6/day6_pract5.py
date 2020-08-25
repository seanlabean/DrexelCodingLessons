import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat

"""
Script for estimating the value of pi from simple Monte Carlo method
"""

#use monte-carlo techniques to solve for pi
N = int(input('Number of points?: '))
#randomly fill unit square
x = np.random.uniform(0,1,N)
y = np.random.uniform(0,1,N)

x_in, y_in = [],[]
for _ in range(N):
	if x[_]**2 + y[_]**2 <= 1.0:
		x_in.append(x[_])
		y_in.append(y[_])
	else:
		continue

PI = (4.0*len(x_in))/N
plt.figure(figsize=(10,10))
plt.scatter(x, y, marker='.', color='r')
plt.scatter(x_in, y_in, marker='o', color='b')
plt.text(0.25,1.05, '$\pi_{estimate} = %.5f$ | $\pi_{true} = %.5f$' % (PI, np.pi),size=20)
pat.Circle(xy=(0,0), radius=1.0, edgecolor='b', linestyle='--', fill=False) #circle boundaries
pat.Rectangle(xy=(0,0),width=1.0,height=1.0, edgecolor='r', linestyle='--', fill=False) #square boundaries
plt.xlabel('x',size=30)
plt.ylabel('y',size=30)
plt.title('Monte Carlo estimate for $\pi$',size=30)
plt.xlim(0,1)
plt.ylim(0,1.1)
plt.tight_layout()
plt.show()
