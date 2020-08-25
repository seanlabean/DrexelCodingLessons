import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.random.normal(5,1.2,N)
y = np.random.uniform(0,1,N)

plt.scatter(x,y, marker='^')
plt.title("Random Points")
plt.xlabel('x position')
plt.ylabel('y position')
plt.tight_layout()
plt.show()
