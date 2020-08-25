import numpy as np
import matplotlib.pyplot as plt

def f(t):
	return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0., 5., .1)
t2 = np.arange(0., 5., .02)

plt.figure(1, figsize=(12,12))
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.title('Subplot 1')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title('Subplot 2')
plt.show()
