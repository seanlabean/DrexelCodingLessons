#Write a function that takes a 1x2 array and an angle X.
#Multiply the array by the rotation matrix R and return the rotated array
#	   
#	R =[cosX	-sinX] 
#	   [sinX	 cosX]

import numpy as np

print("Feed me a 1x2 array: ")
inp = []
for i in range(0,2):
	inp.append(float(input()))
ang = float(input("Now I crave an angle, please: "))
ang2 = ang*np.pi/180.0

mat = np.mat(inp)
R = np.mat(([np.cos(ang2), np.sin(ang2)],[-1*np.sin(ang2), np.cos(ang2)]))

inp_r = inp*R

print('I have rotated your array by your angle')
print(np.around(inp_r,5))

