# Conversión de datos en Python: int(), float(), str()

# Función str(): Convertir datos a string
# La función str() convierte cualquier dato en un string (cadena de texto).
numero = 20
print("Tipo original de 'numero':", type(numero))  # Mostramos el tipo original

# Convertimos el número a string
numero = str(numero)
print("Después de usar str(), 'numero' es de tipo:", type(numero))  # Mostramos el nuevo tipo

# Función int(): Convertir datos a enteros
# La función int() convierte un string o un número decimal a un entero.
numero_como_texto = "654"
numero_entero = int(numero_como_texto)  # Convertimos el string a entero
print("\n----- Usamos la función int() -----")
print("Tipo de 'numero_entero':", type(numero_entero))  # Mostramos el tipo convertido

# Nota: Si intentas convertir un string no numérico, obtendrás un error.
# Por ejemplo: int("Hola") generará un ValueError.

# Función float(): Convertir datos a flotantes
# La función float() convierte un string o un número entero a un número con decimales.
numero_como_texto = "20.3"
numero_flotante = float(numero_como_texto)  # Convertimos el string a flotante
print("\n----- Usamos la función float() -----")
print("Resultado de float('20.3'):", numero_flotante)
print("Tipo de 'numero_flotante':", type(numero_flotante))  # Mostramos el tipo convertido

# Ejemplo práctico: Calculadora de hipotenusa
# Este ejemplo combina entrada de datos, cálculos y conversiones de datos.

print("\n----- Calculadora de Hipotenusa -----")
# Pedimos las longitudes de los catetos al usuario
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))

# Calculamos la hipotenusa usando la fórmula de Pitágoras
hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

# Mostramos el resultado como un string
print("La hipotenusa es: " + str(hipotenusa))
# Salida esperada:
# Si el usuario ingresa 3 y 4, el programa mostrará:
# La hipotenusa es: 5.0

# Nota: Usamos str() para convertir la hipotenusa a string antes de concatenarla con el texto.