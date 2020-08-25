import os
import numpy as np
import matplotlib.pyplot as plt

file = open('../Lesson3/words.txt','r')
Dict = {}

for _ in file:
	if _ in Dict:
		Dict[_] += 1
	else:
		Dict[_] = 1

x = []
y = []

for _ in Dict:
	x.append(_.strip('\n'))
	y.append(Dict[_])

print(Dict)

fig, ax = plt.subplots()
ind = np.arange(len(y))
width = 0.75 #width of bars
ax.barh(ind,y, width, color='b')
ax.set_yticklabels(x, minor=False)
ax.set_yticks(ind+width/2)
plt.title('Word Counts',size=50)
plt.xlabel('Number')
plt.ylabel('Word')
plt.tight_layout()
#plt.savefig(os.path.join('counts.png'), format='png')
plt.show()
