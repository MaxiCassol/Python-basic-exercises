

"""
Escriba un programa que pida tres números y diga si el tercero está más cerca del primero o del segundo.
"""

# Pedir los tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calcular la distancia entre el tercer número y el primero, y entre el tercer número y el segundo
distancia1 = abs(numero3 - numero1)
distancia2 = abs(numero3 - numero2)

# Comparar las distancias y mostrar el resultado
if distancia1 < distancia2:
    print(f"El tercer número ({numero3}) está más cerca del primer número ({numero1}).")
else:
    print(f"El tercer número ({numero3}) está más cerca del segundo número ({numero2}).")
