
import matplotlib.pyplot as plt
from scipy import *
import scipy.integrate as sint

sig = 10.
beta = 8./3
rho = 28.

def drdt(r, t):
	x,y,z = r[0],r[1],r[2]
	dxdt = sig*(y-x)
	dydt = x*(rho-z) - y
	dzdt = x*y - beta*z
	return [dxdt,dydt,dzdt] 

t = arange(0,500,.01)
r0 = array([float(input('x0: ')),float(input('y0: ')) , float(input('z0: '))])

out = sint.odeint(drdt, r0, t)

plt.figure()
plt.plot(out[:,0], out[:,1], 'r.')
plt.xlabel('x')
plt.ylabel('y')
plt.figure()
plt.plot(out[:,1], out[:,2], 'g.')
plt.xlabel('y')
plt.ylabel('z')
plt.figure()
plt.plot(out[:,2], out[:,0], 'b.') 
plt.xlabel('z')
plt.ylabel('x')
plt.show()

