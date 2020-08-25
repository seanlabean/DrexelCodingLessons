import os
import numpy as np
import matplotlib.pyplot as plt

#read in file
f = np.genfromtxt('scores.csv', dtype=None)

#sort by section
S1, S2, S3 = [], [], []
for _ in range(len(f)):
	if f[_][4] == 1:
		S1.append(f[_][2])
	elif f[_][4] == 2:
		S2.append(f[_][2])
	else:
		S3.append(f[_][2])

mu1, sig1 = np.mean(S1), np.std(S1)
mu2, sig2 = np.mean(S2), np.std(S2)
mu3, sig3 = np.mean(S3), np.std(S3)
mut, sigt = np.mean(S1+S2+S3), np.std(S1+S2+S3)

#create 4 subplots
fig = plt.figure(figsize=(12,12))

ax1 = fig.add_subplot(221)
plt.hist(S1,bins='fd',facecolor='r',alpha=0.75)
plt.text(0.8,0.9,'$\mu$ = %.1f, $\sigma$ = %.1f' % (mu1, sig1), ha='center', va='center', transform=ax1.transAxes)
plt.ylabel('Count')
plt.title('Section 1')

ax2 = fig.add_subplot(222)
plt.hist(S2,bins='fd',facecolor='g',alpha=0.75)
plt.text(0.8,0.9,'$\mu$ = %.1f, $\sigma$ = %.1f' % (mu2, sig2), ha='center', va='center', transform=ax2.transAxes)
plt.ylabel('Count')
plt.title('Section 2')

ax3 = fig.add_subplot(223)
plt.hist(S3,bins='fd',facecolor='b',alpha=0.75)
plt.text(0.8,0.9,'$\mu$ = %.1f, $\sigma$ = %.1f' % (mu3, sig3), ha='center', va='center', transform=ax3.transAxes)
plt.ylabel('Count')
plt.xlabel('Scores')
plt.title('Section 3')

ax = fig.add_subplot(224)
plt.hist(S1+S2+S3,bins='fd',facecolor='y',alpha=0.75)
plt.text(0.8,0.9,'$\mu$ = %.1f, $\sigma$ = %.1f' % (mut, sigt), ha='center', va='center', transform=ax.transAxes)
plt.ylabel('Count')
plt.xlabel('Scores')
plt.title('All Sections')

plt.tight_layout()
plt.savefig(os.path.join('score_hists.png'), format='png')

