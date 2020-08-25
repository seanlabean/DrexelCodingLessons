import numpy as np
import matplotlib.pyplot as plt

def log_map(x,a):
	return a-x*x

num_a = 10000
num_discard = 300
num_keep = 1000

a = np.linspace(-0.25, 2, num_a)
x = np.ones_like(a)*0.1

#Call figure to be saved onto
fig= plt.figure()

#Number of transients
for i in range(num_discard):
	x = log_map(x,a)

for i in range(num_keep):
	plt.plot(a,x,'k,')
	x = log_map(x,a)

plt.title("Bifurcation Diagram for Logistic Map")
plt.xlabel('$a$')
plt.ylabel('$x$')

fig.savefig('log.eps')
#plt.show()
