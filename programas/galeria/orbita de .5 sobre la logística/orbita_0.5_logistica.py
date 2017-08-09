__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

def logistic(c, x):
    return c * x * (1 - x)

def evaluate(n, x0, c, f):
    res = x0
    for _ in range(n):
        res = f(c, res)
    return res

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
C = np.linspace(0, 4, 200)
N = np.arange(1, 2001)
X, Y = np.meshgrid(C, N)
#Z = evaluate(Y, .5, X, logistic)
Z = np.empty_like(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = evaluate(Y[i, j], .5, X[i, j], logistic)

ax.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap=cm.jet, linewidth=0,)
plt.show()

