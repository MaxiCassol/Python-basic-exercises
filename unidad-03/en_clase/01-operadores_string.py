# Operadores de Strings en Python

# Concatenación de Strings
# El operador '+' se utiliza para unir (concatenar) dos o más strings.
mensaje_1 = "Hola"
mensaje_2 = "Mundo"
resultado_concatenacion = mensaje_1 + " " + mensaje_2
print("Resultado de la concatenación:", resultado_concatenacion)
# Salida esperada:
# Hola Mundo

# Nota: No se puede concatenar directamente un string con un número.
# Por ejemplo, el siguiente código generaría un error:
# print("Hola" + 5)
# Para evitarlo, se debe convertir el número a string usando str():
numero = 5
print("Hola " + str(numero))  # Esto funciona correctamente.

# Replicación de Strings
# El operador '*' permite repetir un string un número entero de veces.
mensaje = "Python "
resultado_replicacion = mensaje * 3  # Repetimos el string 3 veces
print("Resultado de la replicación:", resultado_replicacion)
# Salida esperada:
# Python Python Python

# Nota: La replicación solo funciona con un string y un número entero.
# Si intentas usar un número decimal, obtendrás un error.
# Por ejemplo, el siguiente código generaría un error:
# resultado = mensaje * 3.3

# Entrada de datos y conversión de tipos
# Solicitamos al usuario que ingrese su edad
edad = input("Por favor, ingresa tu edad: ")

# Convertimos la entrada (que es una cadena) a un entero
edad = int(edad)

# Mostramos el tipo de dato después de la conversión
print("Tipo de dato de 'edad' después de convertir a entero:", type(edad))

# Convertimos la edad a otros tipos de datos
edad_str = str(edad)  # Convertimos a cadena
edad_float = float(edad)  # Convertimos a flotante

# Mostramos los resultados y los tipos de datos
print("Edad como cadena:", edad_str)
print("Tipo de dato de 'edad_str':", type(edad_str))
print("Edad como flotante:", edad_float)
print("Tipo de dato de 'edad_float':", type(edad_float))