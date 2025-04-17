

# 1. Saludo con nombre y edad
nombre = input("1. Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(f"¡Hola, {nombre}! Tienes {edad} años.")

# 2. Figuras geométricas con strings
print("\n2. Figuras geométricas:")
print("+***************+\n" + ("*               *\n" * 3) + "+***************+")
print("\n+---+\n" + ("|   |\n" * 3) + "+---+")
print("\n" + "#" * 35)
print("#" * 35)
print("##" + " " * 31 + "##\n" * 3, end="")
print("#" * 35)
print("#" * 35)

# 3. División de enteros convertidos a float
num1 = int(input("\n3. Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
division = float(num1) / float(num2)
print("Resultado de la división:", division)

# 4. Suma de número ingresado como cadena + 10
cadena = input("\n4. Ingrese un número entero (como texto): ")
resultado = int(cadena) + 10
print("Resultado sumando 10:", resultado)

# 5. Comparación con 10
numero = int(input("\n5. Ingrese un número: "))
if numero > 10:
    print("El número es mayor que 10")
elif numero == 10:
    print("El número es igual a 10")
else:
    print("El número es menor que 10")

# 6. Comparación entre dos números
a = float(input("\n6. Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
if a == b:
    print("Los números son iguales")
else:
    print("Los números son diferentes")

# 7. Mayoría de edad
edad = int(input("\n7. Ingrese su edad: "))
print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")

# 8. Estado del agua según temperatura
temp = float(input("\n8. Ingrese una temperatura en Celsius: "))
if temp >= 100:
    print("El agua está hirviendo")
elif temp <= 0:
    print("El agua está congelada")
else:
    print("El agua está en estado líquido")

# 9. Positivo, negativo o cero
n = float(input("\n9. Ingrese un número: "))
if n > 0:
    print("El número es positivo")
elif n < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 10. Día de la semana
dia = int(input("\n10. Ingrese un número del 1 al 7: "))
dias_semana = {
    1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves",
    5: "Viernes", 6: "Sábado", 7: "Domingo"
}
print(dias_semana.get(dia, "Número de día no válido"))

# 11. Calculadora básica
x = float(input("\n11. Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y if y != 0 else "No se puede dividir por cero")

# 12. Calculadora de IMC
peso = float(input("\n12. Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("Su IMC es:", round(imc, 2))
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

# 13. Conversión Celsius a Fahrenheit
celsius = float(input("\n13. Ingrese temperatura en Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("Temperatura en Fahrenheit:", fahrenheit)

# 14. Juego de adivinanza
numero_secreto = 7
adivinanza = int(input("\n14. Adivina el número (1 al 10): "))
if adivinanza == numero_secreto:
    print("¡Correcto!")
elif adivinanza < numero_secreto:
    print("Demasiado bajo")
else:
    print("Demasiado alto")

# 15. Identificación del tipo de dato
entrada = input("\n15. Ingresa cualquier valor: ")
try:
    valor = int(entrada)
    print("Es un número entero.")
except ValueError:
    try:
        valor = float(entrada)
        print("Es un número flotante.")
    except ValueError:
        print("Es una cadena de texto.")

# 16. Promedio de calificaciones
nota1 = float(input("\n16. Ingrese calificación 1: "))
nota2 = float(input("Ingrese calificación 2: "))
nota3 = float(input("Ingrese calificación 3: "))
promedio = (nota1 + nota2 + nota3) / 3
print("Promedio:", promedio)
print("Aprobado" if promedio >= 6 else "Reprobado")

# 17. Concatenación de nombre y color favorito
nombre = input("\n17. Ingrese su nombre: ")
color = input("Ingrese su color favorito: ")
print(f"Hola {nombre}, tu color favorito es {color}.")


