import numpy as np
import matplotlib.pyplot as plt

#kinematic function
def new_pos(init_d, init_v, accel, time):
	fin_d = init_d + init_v*time + accel*time**2
	return fin_d

#set initial values
x = 0
y = input('Initial height (m), [positive]: ')
v = input('Initial velocity (m/s) [positive] : ')
angle2 = input('Firing angle (deg) (-90 to 90): ')
angle = np.deg2rad(angle2) #recast as radian

x_vals, y_vals = [], []
t = 0
g = 9.81



while y >= 0.0:
	t += 0.0001 #seconds
	x = new_pos(x, v*np.cos(angle), 0, t)
	y = new_pos(y, v*np.sin(angle), -0.5*g, t)
	x_vals.append(x)
	y_vals.append(y)

#plot trajectory
plt.plot(x_vals,y_vals,'r,-')
plt.plot(x_vals, np.zeros(len(x_vals)), 'b--')
plt.text(x_vals[-1]*0.7, (max(y_vals)+1)*0.75, 'angle : %.2f$^{\circ}$ \n tof : %.2f s \n impact: %.1f m' % (angle2, t, x_vals[-1]))
plt.ylabel('y position')
plt.xlabel('x position')
plt.xlim(min(x_vals)-5, max(x_vals)+5)
plt.ylim(-5, max(y_vals)+5)
plt.tight_layout()
plt.show()
