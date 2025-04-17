
"""
Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.

Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).



a	b	c	Solución
1	-2	2	Sin solución real
2	-7	3	Dos soluciones: 0.5 y 3.0
1	2	1	Una solución: -1.0
0	0	5	Sin solución
0	0	0	Todos los números son solución
0	3	2	Una solución: -0.666...


"""
import math

# Solicitar los coeficientes a, b y c
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))
c = float(input("Escriba el valor del coeficiente c: "))

# Verificar los casos especiales
if a == 0:
    if b == 0:
        if c == 0:
            print("Todos los números son solución.")
        else:
            print("Sin solución.")
    else:
        # Ecuación lineal: bx + c = 0
        x = -c / b
        print(f"Una solución: {x}")
else:
    # Ecuación cuadrática: ax² + bx + c = 0
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("Sin solución real.")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Una solución: {x}")
    else:
        # Dos soluciones
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Dós soluciones: {x1} y {x2}")
