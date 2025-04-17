

"""
Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

Nota: Utilice como valor de pi el valor 3.141592.

"""

# Preguntar qué área se desea calcular
opcion = input("¿Quieres calcular el área de un triángulo o un círculo? (T/C): ").lower()

if opcion == "t":
    # Calcular el área de un triángulo
    base = float(input("Escribe la base del triángulo: "))
    altura = float(input("Escribe la altura del triángulo: "))
    area_triangulo = (base * altura) / 2
    print(f"El área del triángulo es: {area_triangulo}")
elif opcion == "c":
    # Calcular el área de un círculo
    radio = float(input("Escribe el radio del círculo: "))
    pi = 3.141592
    area_circulo = pi * (radio ** 2)
    print(f"El área del círculo es: {area_circulo}")
else:
    print("Opción no válida. Por favor, ingresa 'T' para triángulo o 'C' para círculo.")
