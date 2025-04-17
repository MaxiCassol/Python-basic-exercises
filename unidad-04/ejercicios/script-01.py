

"""
Crear una variable con valor 20 va a ser como referencia el minimo.
Otra con valor de 500, va a ser como referencia el maximo.
Luego pregunta al usuario por un valor, almacenarlo en otra variable, forzar a que ponga un numero, sino preguntar repetidamente.
Ese numero transformarlo en integer

Ahora imprimir en pantalla.
Si el numero que puso el usuario es menor que el valor minimo definido mostrar el texto VALOR BAJO
Si el numero que puso el usuario es mayor que el valor maximo definido mostrar el texto VALOR ALTO
Si el numero que puso el usuario esta entre el valor minimo y el valor maximo mostrar el texto VALOR MEDIO
"""


valor_min = 20
valor_max = 500

numero = input("Ingrese un numero: ")
while not numero.isdigit():
    numero = input("Ingrese un numero: ")

# debe continuar acá el programa

print("fin del programa........aun sin resolverlo.")
##############

valor_min = 20
valor_max = 500

# Solicitar al usuario un número, forzando que sea un número entero
numero = input("Ingrese un numero: ")
while not numero.isdigit():  # Repetir hasta que el usuario ingrese un número
    numero = input("Ingrese un numero válido: ")

# Convertir el valor ingresado a entero
numero = int(numero)

# Comprobar en qué rango se encuentra el número y mostrar el mensaje correspondiente
if numero < valor_min:
    print("VALOR BAJO")
elif numero > valor_max:
    print("VALOR ALTO")
else:
    print("VALOR MEDIO")

# Fin del programa
print("fin del programa.")
