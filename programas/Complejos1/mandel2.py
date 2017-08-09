# MANDELBROT SET
import numpy as np
import pylab as pl
 
# number of iterations
iterations = 100
 
# density of the grid
density = 1000


def mandelbrot():
    x_min, x_max = -2, 1
    y_min, y_max = -1.5, 1.5
    #x_min, x_max = -.02, -.01
    #y_min, y_max = -.004, .004
    
    #x, y = np.ogrid[x_min:x_max:density*1j,y_min:y_max:density*1j]
    x, y = np.linspace(x_min, x_max, density)[np.newaxis].T, np.linspace(y_min, y_max, density)
    c = x + 1j * y
    z = c.copy()
    m = np.zeros((density, density))

    for n in range(iterations):
        print("%d %% completado..." % (100 * float(n)/iterations))
        indices = (abs(z) <= 10)
        z[indices] = z[indices]**2 + c[indices]
        m[indices] = n
 
    pl.imshow(np.log(m.T), cmap=pl.cm.hot, extent=(x_min, x_max, y_min, y_max))
 
    pl.title('Mandelbrot Set')
    pl.xlabel('Re(z)')
    pl.ylabel('Im(z)')
    pl.show()


def julia(c):
    x_min, x_max = -2, 2
    y_min, y_max = -1.5, 1.5
    
    #x, y = np.ogrid[x_min:x_max:density*1j, y_min:y_max:density*1j]
    x, y = np.linspace(x_min, x_max, density)[np.newaxis].T, np.linspace(y_min, y_max, density)
    
    z = x + 1j * y
    m = np.zeros((density, density))
    
    for n in range(iterations):
        indices = (abs(z) <= 10)
        z[indices] = z[indices]**2 + c
        m[indices] = n
 
    pl.imshow(np.log(m.T), cmap=pl.cm.hot, extent=(x_min, x_max, y_min, y_max))
 
    pl.title('Julia Set')
    pl.xlabel('Re(z)')
    pl.ylabel('Im(z)')
    pl.show()
    
#julia(2j)
mandelbrot()
#julia(-.8j)