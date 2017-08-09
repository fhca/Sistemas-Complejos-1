__author__ = 'fhca'

from tkinter import *
from numpy import *

n = 100

xmin = -pi
xmax = pi

ymin = -1
ymax = 1

dx = (xmax - xmin) / (n - 1)  # ancho de la subdivisión

alto = 1900 / pi
ancho = pi * alto

canvas = Canvas(width=ancho, height=alto, bg='white')
canvas.pack(expand=YES, fill=BOTH)


xpmin = ancho / 10
xpmax = ancho - xpmin
ypmin = alto / 10
ypmax = alto - ypmin

def transf(z, zmin, zmax, zpmin, zpmax):
    return (z - zmin)/(zmax - zmin) * (zpmax - zpmin) + zpmin

canvas.create_rectangle(xpmin, ypmin, xpmax, ypmax, outline="black", fill="white")

X = arange(xmin, xmax + dx, dx)
Y = sin(X)

XP = transf(X, xmin, xmax, xpmin, xpmax)
YP = transf(Y, ymin, ymax, ypmin, ypmax)

for i in range(1, n):
    canvas.create_line(XP[i-1], YP[i-1], XP[i], YP[i], fill="blue")

mainloop()