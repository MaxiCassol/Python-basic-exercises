# Detector de Palíndromos:

# Desarrolla un programa que verifique si una palabra ingresada por el usuario es un palíndromo (una palabra que se lee igual de adelante hacia atrás). El proceso es el siguiente:
# Pide al usuario que ingrese una palabra.
# Utiliza un bucle for junto con índices para recorrer la mitad del string y comparar los caracteres desde el principio con los caracteres desde el final.
# Si todos los caracteres coinciden, indica que la palabra es un palíndromo; de lo contrario, indica lo contrario.

# Detector de Palíndromos

# Pedir al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ").lower()  # Convertimos a minúsculas para comparar sin distinguir mayúsculas

es_palindromo = True  # Suponemos que lo es, hasta que se demuestre lo contrario

# Recorrer solo hasta la mitad de la palabra
for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-(i + 1)]:  # Comparamos desde el inicio y el final
        es_palindromo = False
        break  # Salimos si encontramos una diferencia

# Mostrar el resultado
if es_palindromo:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
