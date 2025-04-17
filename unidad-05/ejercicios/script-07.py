# Contador de Caracteres Específicos:

# Crea un programa que solicite al usuario ingresar una letra o carácter. El programa debe contar y mostrar cuántas veces aparece ese carácter en una frase dada. El procedimiento es el siguiente:
# Pide al usuario que ingrese una frase.
# Luego, pide al usuario que ingrese un carácter para buscar en la frase.
# Utiliza un bucle for junto con índices para recorrer la frase y contar las ocurrencias del carácter especificado.
# Muestra el número total de veces que aparece ese carácter en la frase.


# Contador de Caracteres Específicos

# Solicitar al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Solicitar al usuario que ingrese un carácter para buscar
caracter = input("Ingrese un carácter a buscar: ")

# Validación para asegurarse de que ingresó solo un carácter
while len(caracter) != 1:
    caracter = input("Por favor, ingrese solo UN carácter: ")

# Contador de ocurrencias
contador = 0

# Recorrer la frase con un bucle for usando índices
for i in range(len(frase)):
    if frase[i] == caracter:
        contador += 1

# Mostrar el resultado
print(f"El carácter '{caracter}' aparece {contador} veces en la frase.")
