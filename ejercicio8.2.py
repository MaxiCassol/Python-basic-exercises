from pickle import *

f = open('mifichero.py', 'w+b')

class Vehiculo:
    motor: ""
    cilindrada: ""

    def __init__(self, motor, cilindrada):
        self.motor = motor
        self.cilindrada = cilindrada

    def __str__(self):
        return self.motor + " " + self.cilindrada

auto1 = Vehiculo("Diesel", "2.0")
print(auto1)

f = open('Vehiculo', 'w+b')

dump(auto1, f)

f.seek(0)
nuevo_auto1 = load(f)

print(nuevo_auto1)
f.close()