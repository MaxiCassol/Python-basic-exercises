

"""
Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.

Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones):

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 0
Escriba el valor del coeficiente b: 3
La ecuación no tiene solución.

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 4.2
Escriba el valor del coeficiente b: 21
La ecuación tiene una solución: -5.0

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 0
Escriba el valor del coeficiente b: 0
Todos los números son solución.

"""

# Solicitar los coeficientes a y b
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))

# Evaluar las condiciones
if a == 0:
    if b == 0:
        print("Todos los números son solución.")
    else:
        print("La ecuación no tiene solución.")
else:
    # Calcular la solución única x = -b / a
    x = -b / a
    print(f"La ecuación tiene una solución: {x}")
