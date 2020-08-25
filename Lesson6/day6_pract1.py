import matplotlib.pyplot as plt
import numpy as np

"""
Script to plot the trajectory of a cannonball, given inital height, angle, and velocity

"""
def fin_loc(init_pos, init_vel, accel, t):
	return init_pos + init_vel*t + accel*t**2

height = float(input('Initial height? (positive): '))
vel = float(input('Initial velocity? (positive): '))
angle = float(input('Firing angle? (degrees): '))
g = 9.81 #m/s**2

tof = max(np.roots([-0.5*g, vel*np.sin(np.deg2rad(angle)), height]))
x_fin = fin_loc(0, vel*np.cos(np.deg2rad(angle)), 0, tof)

print('time of flight is %f seconds' % tof)
print('point of impact is %.1f meters' % x_fin)


t_vals = np.linspace(0, tof, 1000)
x_vals = [fin_loc(0, vel*np.cos(np.deg2rad(angle)), 0, _ ) for _ in t_vals]
y_vals = [fin_loc(height, vel*np.sin(np.deg2rad(angle)), -0.5*g, _ ) for _ in t_vals]

plt.plot(x_vals, y_vals, 'r--') 
plt.plot([min(x_vals)-5,max(x_vals)+5], [0,0],'b-') #water
plt.fill_between([min(x_vals)-5,max(x_vals)+5],[0,0],[-5,-5]) #color the water, I'm fancy
plt.plot([0,0],[0,height],'ko-') #hill
plt.xlim(min(x_vals)-5, max(x_vals)+5)
plt.ylim(-5,max(y_vals)+5)
plt.title('Cannonball Trajectory')
plt.xlabel('x position [m]')
plt.ylabel('y position [m]')
plt.tight_layout()
plt.grid(True)
plt.show()
