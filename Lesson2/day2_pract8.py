#Write a function that computes the factorial of its input

import math as m

#lazy way
#def Fac(x):
#	return m.factorial(x)

#nonlazy way
def nlFac(x):
	"""
	Computes factorial of x non-recursively
	"""
	if x < 0:
		return "Error!, non-negative numbers please"

	if x - int(x) != 0:
		return "Error!, integers only please"

	if x == 0:
		return 1

	ret = 1
	for i in range(1, x+1):
		ret *= i
	return ret

def Fac_r(x):
	
	if x < 0:
		return 0
	
	if x == 0:
		return 1

	else:
		return x * Fac_r(x-1)
#Test

for i in range(10):
	print("%d! = %d" % (i, Fac_r(i)))
