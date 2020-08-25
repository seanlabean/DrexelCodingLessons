import os
import csv
import numpy as np


N = 101 #number of students

#out1 = open('scores.csv','w')

fnames = ['Chris','Alex','John','Mary', 'Kim','Ryan','Vince','Olga', 'Harry', 'Wendy', 'Lori','Tom','Alicia','Paula','Tanya']
lnames = ['A.','M.','F.','D.','S.','P.','T.','N.','M.','O.','H.']
sect = ['Section 1', 'Section 2', 'Section 3']

names = []
section = []
for _ in range(N):
	c1 = np.random.randint(0,len(fnames),1)[0]
	c2 = np.random.randint(0,len(lnames),1)[0]
	names.append(fnames[c1]+' '+lnames[c2])
	section.append(sect[np.random.randint(0,len(sect),1)[0]])

scores = np.random.normal(80,10,N) + np.random.randint(-5,11,N)
scores = np.around(scores,4)

with open('scores.csv','w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(zip(names,scores,section))
