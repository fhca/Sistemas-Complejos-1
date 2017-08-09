__author__ = 'fhca'

from tkinter import *
from math import *

n = 100
Pi = 3.14159265

xmin = -Pi
xmax = Pi

ymin = -1
ymax = 1

x0 = xmin
x = x0
dx = (xmax - xmin) / (n - 1)  # ancho de la subdivisión

alto = 1900 / Pi
ancho = Pi * alto

canvas = Canvas(width=ancho, height=alto, bg='white')
canvas.pack(expand=YES, fill=BOTH)

y = sin(x)

xant = x
yant = y

xpmin = ancho / 10
xpmax = ancho - xpmin
ypmin = alto / 10
ypmax = alto - ypmin

def transf(z, zmin, zmax, zpmin, zpmax):
    return (z - zmin)/(zmax - zmin) * (zpmax - zpmin) + zpmin

canvas.create_rectangle(xpmin, ypmin, xpmax, ypmax, outline="black", fill="white")

X = [x + i * dx for i in range(n)]
Y = [sin(x) for x in X]

XP = [transf(x, xmin, xmax, xpmin, xpmax) for x in X]
YP = [transf(y, ymin, ymax, ypmin, ypmax) for y in Y]

for i in range(1, n):
    canvas.create_line(XP[i-1], YP[i-1], XP[i], YP[i], fill="blue")

mainloop()