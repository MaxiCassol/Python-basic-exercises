# Juego de Adivinar el Número Secreto:
# Desarrolla un programa en el que la computadora elija un número aleatorio entre 1 y 100. El usuario deberá intentar adivinar ese número. El programa debe proporcionar pistas, después de cada intento del usuario hasta que adivine correctamente.
# Con respecto a las pistas, si bien está abierto a como quieras resolverlo la idea es ir avisando si está muy alejado, mas o menos alejado, cerca, muy cerca, etc. Pudiendo avisar si el número es mayor o menor al que se intenta adivinar.

import random

# Generar el número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializamos el número de intentos
intentos = 0

print("Bienvenido al juego de Adivinar el Número Secreto.")
print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

# Bucle principal del juego
while True:
    intento = input("Ingresa tu intento: ")

    # Verificamos si la entrada es un número válido
    if not intento.isdigit():
        print("Por favor, ingresa un número válido.")
        continue

    intento = int(intento)
    intentos += 1

    # Verificar si el número adivinado es correcto
    if intento == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número secreto en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        diferencia = numero_secreto - intento
        if diferencia > 50:
            print("¡Estás muy lejos! El número secreto es mucho mayor.")
        elif diferencia > 20:
            print("¡Estás lejos! El número secreto es un poco mayor.")
        elif diferencia > 5:
            print("¡Estás cerca! El número secreto es un poco mayor.")
        else:
            print("¡Estás muy cerca! Solo un poco más.")
    else:
        diferencia = intento - numero_secreto
        if diferencia > 50:
            print("¡Estás muy lejos! El número secreto es mucho menor.")
        elif diferencia > 20:
            print("¡Estás lejos! El número secreto es un poco menor.")
        elif diferencia > 5:
            print("¡Estás cerca! El número secreto es un poco menor.")
        else:
            print("¡Estás muy cerca! Solo un poco más.")



