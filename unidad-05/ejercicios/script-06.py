# Crea un programa que permita al usuario calcular el área y el perímetro de varias figuras geométricas. El programa debe presentar un menú con las siguientes opciones:

# Calcular el área y el perímetro de un círculo.
# Calcular el área y el perímetro de un cuadrado.
# Calcular el área y el perímetro de un triángulo.
# Salir del programa.





# Área y Perímetro de un Círculo:
    # Área del círculo: Área = π × radio²
    # Perímetro del círculo: Perímetro = 2 × π × radio
# Área y Perímetro de un Cuadrado:
    # Área del cuadrado: Área = lado²
    # Perímetro del cuadrado: Perímetro = 4 × lado
# Área y Perímetro de un Triángulo:
    # Área del triángulo: Área = 0.5 × base × altura
    # Perímetro del triángulo: Suma de los 3 lados


import math

def menu():
    print("""
--- Calculadora de Área y Perímetro ---
1. Círculo
2. Cuadrado
3. Triángulo
4. Salir
""")

def circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")

def cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print(f"Área del cuadrado: {area:.2f}")
    print(f"Perímetro del cuadrado: {perimetro:.2f}")

def triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    lado1 = float(input("Ingrese el lado 1 del triángulo: "))
    lado2 = float(input("Ingrese el lado 2 del triángulo: "))
    lado3 = float(input("Ingrese el lado 3 del triángulo: "))
    area = 0.5 * base * altura
    perimetro = lado1 + lado2 + lado3
    print(f"Área del triángulo: {area:.2f}")
    print(f"Perímetro del triángulo: {perimetro:.2f}")

# Programa principal
while True:
    menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        circulo()
    elif opcion == "2":
        cuadrado()
    elif opcion == "3":
        triangulo()
    elif opcion == "4":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
