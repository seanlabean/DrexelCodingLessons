#Read the comma separated file 'numbers.cvs' and store the 1st and 4th column in a list

import string

#Read in file

infile = open('numbers.cvs')

#create empty list for each column

col1 = []
col4 = []

for line in infile:
	#strips whitespace
	line = line.strip()
	#splits at comma
	data = line.split(',')
	#append 0th element to col1
	col1.append(data[0])
	#append 3rd element to col4
	col4.append(data[3])
	print(data[0], data[3])

