#Read words from 'words.txt' and count how many times they occur

import numpy as np

#Read in words.txt

file = open('words.txt', 'r')

#Create empty Dictionary
Dict = {}

for i in file:
	if i in Dict:
		Dict[i.strip('\n')] += 1
	else:
		Dict[i.strip('\n')] = 1

print(Dict)



