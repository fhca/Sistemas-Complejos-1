__author__ = 'fhca'

class Carro:

    def __init__(self,marca="Honda",modelo="2015",color="azul"):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = 0
        self.actualiza_descripcion()

    def actualiza_descripcion(self):
        self.descripcion = "El carro "+self.marca+" " +self.color+" modelo "+self.modelo+" tiene un kilometraje de "+str(self.kilometraje)

    def cambia_color(self,colorn):
        self.color = colorn
        self.actualiza_descripcion()

    def avanza(self,km):
        self.kilometraje = self.kilometraje + km
        self.actualiza_descripcion()

    def muestra(self):
        print(self.descripcion)


c1 = Carro()
c2 = Carro(color = "blanco")
c3 = Carro("Mazda","2016","negro")

c2.avanza(20)
c2.avanza(50)

#c3.cambia_color("blanco")

c1.muestra()
c2.muestra()
c3.muestra()

