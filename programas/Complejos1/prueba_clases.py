__author__ = 'fhca'

class Cuadrado:

    def __init__(self, l=10):
        self.base = l
        self.descripcion = "cuadrado con base "+str(self.base)

    def perimetro(self):
        return 4 * self.base

    def area(self):
        return self.base ** 2

class Rectangulo(Cuadrado):
    def __init__(self, b=10, a=5):
        self.base = b
        self.altura = a
        self.descripcion = "rectangulo con base "+str(self.base)+" y altura "+str(self.altura)

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo:
    def __init__(self, b=10, a=5):
        self.base = b
        self.altura = a
        self.actualiza_descripcion()

    def actualiza_descripcion(self):
        self.descripcion = "triangulo con base "+str(self.base)+" y altura "+str(self.altura)

    def cambia_altura(self, anueva):
        self.altura = anueva
        self.actualiza_descripcion()

    def cambia_base(self, bnueva):
        self.base = bnueva
        self.actualiza_descripcion()

    def perimetro(self):
        pass

    def area(self):
        return self.base * self.altura / 2

c1 = Cuadrado()
r1 = Rectangulo()
t1 = Triangulo()

t1.cambia_altura(7)
t1.cambia_base(3)

def muestra(c):
    print("El", c.descripcion, "tiene area", c.area())

#print("El cuadrado de lado ", c1.base, " tiene área:", c1.area(), " y perimetro:", c1.perimetro())
#print("El rectangulo de base", r1.base, " y altura ", r1.altura, " tiene area ", r1.area(), " y perimetro:", r1.perimetro())
#print("El triangulo de base",t1.base, "y altura", t1.altura, "tiene area",t1.area())

muestra(c1)
muestra(r1)
muestra(t1)