__author__ = 'fhca'

"Construir una lista con los cuadrados de los prineros 100 enteros positivos."

l = []
for i in range(1, 11):
    l.append( i ** 2)
print(l)

m = [x ** 2 for x in range(1, 11)]
print(m)

t = (x ** 2 for x in range(1, 11))

for x in t:
    print("el siguiente es: ", x)