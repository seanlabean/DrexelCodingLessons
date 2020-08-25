import numpy as np

p = 0
q = 100
N = 100
a = np.linspace(p, q, N)


def built_in():
	return sum(a)

def numpy():
	return np.sum(a)

def unitary():
	return a.sum()

if __name__ == "__main__":
	import timeit
	
	# Number of test case
	N = 1000

	t = timeit.timeit("unitary()", setup="from __main__ import unitary", number = N)
	print("Unitary took %g" % t)

	t = timeit.timeit("numpy()", setup="from __main__ import numpy")
	print("Numpy took %g" % t)

	t = timeit.timeit("built_in()", setup="from __main__ import built_in")
	print("Built-In took %g" % t)
