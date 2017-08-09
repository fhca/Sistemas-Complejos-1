__author__ = 'fhca'

import matplotlib.pyplot as plt
from numpy import *
import matplotlib.animation as animation

n = 100

xmin = -pi
xmax = pi

ymin = -1
ymax = 1

dx = (xmax - xmin) / (n - 1)  # ancho de la subdivisión

X = arange(xmin, xmax + dx, dx)

fig, ax = plt.subplots()
dibujo, = ax.plot([], [])

def init():
    dibujo, = ax.plot(sin(X), "b-")

def run(datos):
    dibujo.set_data(X, sin(X + datos))

a = animation.FuncAnimation(fig, run, (x for x in arange(0, 2*pi, 100)), blit=False, interval=10, init_func=init)



plt.ylabel("f(x)")
plt.show()
