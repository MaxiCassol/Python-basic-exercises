





import math

# 1. Área de un rectángulo
base = 5
altura = 3
area_rectangulo = base * altura
print("1. Area del rectangulo:", area_rectangulo)

# 2. Conversión Celsius a Fahrenheit
celsius = float(input("2. Ingrese temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperatura en Fahrenheit:", fahrenheit)

# 3. Concatenar nombre y edad como strings y mostrar tipo
nombre = "Maximiliano"
edad = "30"
nombre_edad = nombre + edad
print("3. Nombre y edad concatenados:", nombre_edad)
print("Tipo de dato:", type(nombre_edad))

# 4. Área de un círculo
radio = 4
area_circulo = math.pi * radio**2
print("4. Área del círculo:", area_circulo)

# 5. Operaciones entre dos números ingresados por el usuario
num1 = float(input("5. Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2 if num2 != 0 else "División por cero no permitida")

# 6. Operación aritmética compleja
resultado_complejo = ((5 + 3) * 2 - 4) / 2
print("6. Resultado operación compleja:", resultado_complejo)
print("Tipo de dato:", type(resultado_complejo))

# 7. Variable booleana de estado del examen
aprobado = True
print("7. ¿El alumno aprobó?", aprobado)

# 8. Perímetro de un triángulo equilátero
lado = 6
perimetro_triangulo = 3 * lado
print("8. Perímetro del triángulo equilátero:", perimetro_triangulo)

# 9. Datos del usuario
nombre_usuario = input("9. Ingrese su nombre: ")
edad_usuario = int(input("Ingrese su edad: "))
ciudad_usuario = input("Ingrese su ciudad de residencia: ")
print("Nombre:", nombre_usuario, "| Tipo:", type(nombre_usuario))
print("Edad:", edad_usuario, "| Tipo:", type(edad_usuario))
print("Ciudad:", ciudad_usuario, "| Tipo:", type(ciudad_usuario))

# 10. Operación matemática con paréntesis, multiplicación, suma y resta
operacion = (10 + 5) * 3 - 8
print("10. Resultado:", operacion)
print("Tipo de dato:", type(operacion))
