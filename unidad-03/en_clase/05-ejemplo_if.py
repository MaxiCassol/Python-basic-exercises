




alumno_nombre = input("Inserte el nombre del alumno: ")
alumno_edad = int(input("Inserte la edad del alumno: "))



if alumno_edad >= 18 and alumno_edad <= 21:
    # Este bloque de código se ejecuta si la condición es verdadera
    print("El alumno", alumno_nombre, "tiene entre 18 y 21 años")
elif alumno_edad >= 22 and alumno_edad <= 30:
    # Este bloque de código se ejecuta si la condición anterior es falsa y esta es verdadera
    print("El alumno", alumno_nombre, "tiene entre 22 y 30 años")
elif alumno_edad >= 31 and alumno_edad <= 40:
    # Este bloque de código se ejecuta si la condición anterior es falsa y esta es verdadera
    print("El alumno", alumno_nombre, "tiene entre 31 y 40 años")
else:
    # Este bloque de código se ejecuta si la condición anterior es falsa y esta es verdadera
    print("El alumno", alumno_nombre, "tiene más de 40 años")

exit()
# elif alumno_edad >= 16:
#     # Este bloque de código se ejecuta si la condición anterior es falsa y esta es verdadera
#     print("El alumno", alumno_nombre, "es menor de edad pero puede manejar")
#     print("Puede manejar")
#     print("No puede votar")
# elif alumno_edad >= 14:
#     # Este bloque de código se ejecuta si la condición anterior es falsa y esta es verdadera
#     print("El alumno", alumno_nombre, "es menor de edad pero puede manejar")
#     print("NO Puede manejar")
#     print("No puede votar")
#     print("No puede comprar alcohol")
# else:
#     # Este bloque de código se ejecuta si la condición es falsa
#     print("El alumno", alumno_nombre, "es menor de edad")
#     print("No puede votar")
#     print("No puede manejar")


# print("El programa sigue ejecutándose...")

exit()






























alumno_nombre = "Juan"
alumno_edad = 17

if alumno_edad >= 18:
    print("El alumno", alumno_nombre, "es mayor de edad")
else:
    print("El alumno", alumno_nombre, "es menor de edad")




edad = int( input("Escribí tu edad: ") )


if edad >= 18:
    # acá empieza el bloque de codigo si la condicion es verdadera
    print("Sos mayor de edad")
    print("Podes votar")
    print("Podes manejar")
    print("Podes comprar alcohol")
    print("Podes ir a la carcel")
    # fin del bloque
else:
    # este es el principio del bloque de codigo si la condicion es falsa
    if edad >= 16:
        print("Sos menor de edad")
        print("Si estas en CABA podes sacar el registro")
        exit()
    else:
        numero = 2 + 2
    
    # sigue acá


print("Esto lo ejecuta en todos los casos.......")













# Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si
# la división es exacta o no.


numero_uno = int(input("Ingrese el primer numero: "))

numero_dos = int(input("Ingrese el segundo numero: "))

resultado = numero_uno % numero_dos

if resultado == 0:
    print("El resultado es exacto")
else:
    print("El resultado no es exacto, el resto es", resultado)



