__author__ = 'fhca'

import matplotlib.pyplot as plt
from numpy import *

n = 100

xmin = -pi
xmax = pi

dx = (xmax - xmin) / (n - 1)  # ancho de la subdivisión

X = arange(xmin, xmax + dx, dx)

plt.plot(sin(X), "b-")
plt.ylabel("f(x)")
plt.show()