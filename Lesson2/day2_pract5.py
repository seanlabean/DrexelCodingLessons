#Calculate cos(x) for x in range(0,2pi) in 0.1 step increments

import math as m

X=[]
i = 0

while i <= 2*m.pi:
	X.append(i)
	i = i + 0.1

print("x from 0 to 2pi")
print(X)

#create list of Cos(x) values
COS = [m.cos(i) for i in X]

print("Calculated Cos(x)")
print(COS)

#SAME AS THIRD OPTION SHOWN BY INSTRUCTOR

#NOTE - Numbers vary from other methods because of computer storing processes (variables storage depending on bits)
#check epsilon = 10e-6, if abs(var - 0.4) < eps
