#Write a function that computes f(x) = x**3 + x*e**x + 1 and applies to to all the elements in an array

import numpy as np

#take in an array
print('Feed me an array... W_[OmO]_W ')
n = int(input('Number of elements: '))
ARR = []
for i in range(0,n):
	ele = float(input())
	ARR.append(ele)
ARR = np.array(ARR)

#Function defined
def F_x(x):
	return  x**3 + x*np.exp(x) + 1

ANS = F_x(ARR)

print('Your array: ')
print(ARR)
print('Your answer: ')
print(ANS)
