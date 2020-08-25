#Write a function for the Tent Map given in Practical 7

def F(x):
	"""
	Tent Map Function

	This function computes the tent map

	x must be a number
	"""
	if 0 < x < 1:
		return x
	elif 1 < x < 2:
		return 2 - x
	else:
		return 0.0

#-------------------------------------------------

#Call Function

dx = 0.1
start = 0
stop = 2.0

while start < stop:
	print("f(%g) = %g " % (start, F(start)))
	start += dx


