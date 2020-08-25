import scipy as sc
import matplotlib.pyplot as plt
import os

"""
Script for reading in a junk file and sorting values into strings or numbers. 

"""

file = open('junk.txt','r')

#lazy alphabet
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','o','p','q','r','s','t','u','v','w','x','y','z',]
ListA, ListB = [], []

#read in each entry, with conditions
counter = 0
for line in file:
	counter +=1
#if entry is integer, append ListA
	linestrip = line.strip()
	if linestrip.isdigit() == True:
		ListB.append(int(line.strip()))
#if entry starts with alphabetical value
	elif line.strip()[0] in alph:
		ListA.append(line.strip())
#else skip it
	else:
		continue

#Dictionary for ListA, plot barchart as previous
Dict = {}

for _ in ListA:
	if _ in Dict:
		Dict[_] += 1
	else:
		Dict[_] = 1

x,y = [],[]

for _ in Dict:
	x.append(_.strip('\n'))
	y.append(Dict[_])

fig, ax = plt.subplots()
ind = sc.arange(len(y))
width = 0.75 #width of bars
ax.barh(ind,y, width, color='b')
ax.set_yticklabels(x, minor=False)
ax.set_yticks(ind+width/2)
plt.title('Word Counts')
plt.xlabel('Number')
plt.ylabel('Word')
plt.tight_layout()

#Numerical Analysis of ListB
print('----------------------------------------------')

B = sc.array(ListB)
print('Total numbers: ', len(ListB))
print('Mean: ', B.mean())
print('Median: ', sc.median(B))
print('Standard Deviation: ', B.std())

print('-----------------------------------------------')
#Save ListA to file
outA = open('words_sorted.txt','w')
for _ in sc.sort(ListA):
	print(_, file=outA)
outA.close()
#Save ListB to file
outB = open('num_sorted.txt','w')
for _ in sc.sort(ListB):
	print(_, file=outB)
outB.close()

#plot last
plt.show()
