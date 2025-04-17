


"""
Pedir al usuario que ingrese un número de inicio del bucle
Pedir al usuario que ingrese un número de fin del bucle
Validar que el número de inicio sea menor al número de fin, si no es así volver a pedir los dos números, hasta que ésto sea correcto
Luego de que el usuario ingrese los dos números, mostrar en pantalla todos los números que hay entre el número de inicio y el número de fin
De la siguiente manera:
Este es el bucle número 1
Este es el bucle número 2
Este es el bucle número 3
---
Fin del programa.

"""

while True:
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número de fin: "))
    
    if inicio < fin:
        break  

    print("El número de inicio debe ser menor al número de fin. Por favor, intente de nuevo.")

for i in range(inicio, fin + 1):
    print(f"Este es el bucle número { i }")

print("Fin del programa.")
