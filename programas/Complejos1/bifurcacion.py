__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import cm

def logistic(c, x):
    return c * x * (1 - x)

fig = plt.figure()
ax = fig.add_subplot(111)

N=1000  # N x N square window, (resolution)
C = np.linspace(3.54, 3.58, N)
Y = np.array([0.5] * N)
for _ in range(500):
    Y = logistic(C, Y)  # wasted initial values
for _ in range(N):
    Y = logistic(C, Y)
    ax.plot(C, Y, 'k,')
plt.show()
