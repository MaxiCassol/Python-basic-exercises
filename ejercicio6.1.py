class Vehiculo:
    color = "azul"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 1.6

c = Coche()
print(c.color, c.ruedas, c.puertas, c.velocidad, c.cilindrada)