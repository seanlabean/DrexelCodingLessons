import numpy as np
import os

junk = []

#create list of words
words = ['cow','brown','happy','goat','house','fluffy','zebra','linux','moose','cat','zebra']

#create 'junk' strings

strops = ['%','&','(','#','&','^']

file = open('junk.txt','w')

for _ in range(10000):
	call = np.random.randint(0,3,1)
	if call == 0:
		x = words[np.random.randint(0,len(words),1)[0]]
		print >> file, x
	elif call == 1:
		x = np.random.randint(1,200,1)[0]
		print >> file, x
	else:
		x1 = strops[np.random.randint(0,len(strops),1)[0]]
                x2 = strops[np.random.randint(0,len(strops),1)[0]]
                x3 = strops[np.random.randint(0,len(strops),1)[0]]
                x4 = strops[np.random.randint(0,len(strops),1)[0]]
                x5 = strops[np.random.randint(0,len(strops),1)[0]]
                x6 = strops[np.random.randint(0,len(strops),1)[0]]
		x = x1+x2+x3+x4+x5+x6
		print >> file, x

file.close()

