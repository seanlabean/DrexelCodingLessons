import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
plt.hist(x,50, density=True, facecolor='r', alpha=0.5)
plt.hist(x,30, density=True, facecolor='g', alpha=0.5)
xl, xu = plt.xlim()

#windowdressing
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.025, '$\mu=100,\ \sigma=15$')
plt.tight_layout()
plt.grid(True)
plt.xlim(xl,xu)
plt.show()
