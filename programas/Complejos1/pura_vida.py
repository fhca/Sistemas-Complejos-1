__author__ = 'fhca'

import numpy as np
from matplotlib.pyplot import figure, show
from matplotlib import cm
import matplotlib.animation as animation

""" juego de la vida """

class AC:
    def __init__(self, mx, my, inicial):
        fig = figure()
        self.ax = fig.add_subplot(111)
        self.X = np.zeros((mx, my, 2), dtype=np.bool)  # 2 matrices llenas de ceros
        #ax.set_title("usar scroll para navegar las reglas")
        self.alto, self.ancho, self.slices = mx, my, 2  # dimensiones
        self.ind = 0  # indicador de la matriz actual a utilizar
        if inicial == "iterador":  # ejemplo de estructuras
            self.X[0:3, 1, 0] = 1
        elif inicial == "glider":
            self.X[0, 1, 0] = self.X[1, 2, 0] = self.X[2, 0:3, 0] = 1
        elif inicial == "eloy":
            self.X[0,0,0] = self.X[0, 1, 0] = self.X[1, 0, 0] = self.X[1, 1, 0] = 1
            self.X[4, 3:6, 0] = self.X[5, 4:7, 0] = 1
        elif inicial=="tere":
            self.X[0, 3, 0]=self.X[1, 0, 0]=self.X[1, 2, 0] = self.X[2, 1, 0] = \
                self.X[2, 3, 0] = self.X[3, 4, 0]=self.X[4, 2, 0] = 1
        elif inicial == "azar":
            self.X[:, :, 0] = np.round(np.random.random((mx, my)))
        self.im = self.ax.imshow(self.X[:, :, self.ind], cmap=cm.Blues)  # crea el 1er dibujo
        animation.FuncAnimation(fig, self.actualiza, self.aplica_regla,  # crea animación
                                blit=False, interval=10, repeat=True)
        show()

    def aplica_regla(self):
        this = self.ind  # esta matriz
        other = 1 - this  # la siguiente
        m = self.X
        for x in range(self.alto):
            for y in range(self.ancho):
                px, nx = (x + self.alto - 1) % self.alto, (x + 1) % self.alto  # previa y sig. x y y
                py, ny = (y + self.ancho - 1) % self.ancho, (y + 1) % self.ancho
                vecinos = 0 + m[px, py, this] + m[x, py, this] + m[nx, py, this] + \
                          m[px, ny, this] + m[x, ny, this] + m[nx, ny, this] + \
                          m[px, y, this] + m[nx, y, this]  # suma de vecinos
                if vecinos == 3:  # 3 vecinos, nace
                    m[x, y, other] = 1
                elif vecinos == 2:  # 2 vecinos, continua
                    m[x, y, other] = m[x, y, this]
                else:  # otros, muere
                    m[x, y, other] = 0
        self.ind = other  # se pasa a la siguiente matriz
        yield 0

    def actualiza(self, _=0):
        "Requiere un parámetro, pero no lo utilizamos."
        self.im.set_data(self.X[:, :, self.ind])  # los datos ahora son los de la otra matriz

a = AC(5, 5, "tere")
