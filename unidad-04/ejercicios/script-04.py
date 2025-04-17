


"""
Vamos a realizar un programa que nos va a decir la nota promedio de un alumno en todo el cuatrimestre.
Dentro del cuatrimestre son 4 examenes y luego un examen final.
La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o más de 6 de promedio en sus 4 examenes, rinde el examen final)
Si el alumno tiene aprobada la cursada y el examen final, entonces el alumno aprobó la materia.

Entonces el programa debe preguntar por la nota de cada examen.
En función de las respuestas, primero debe avisar el promedio de las 4 notas de los examenes.
En caso de que el promedio sea mayor o igual a 6, debe avisar que el alumno tiene aprobada la cursada.
En caso de que el promedio sea menor a 6, debe avisar que el alumno no tiene aprobada la cursada.
Luego preguntar por nota del final (en caso de que haya aprobado la cursada), si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de la materia, y puede rendir recuperatorio.



"""

# Solicitar las notas de los 4 exámenes
nota1 = float(input("Ingrese la nota del examen 1: "))
nota2 = float(input("Ingrese la nota del examen 2: "))
nota3 = float(input("Ingrese la nota del examen 3: "))
nota4 = float(input("Ingrese la nota del examen 4: "))

# Calcular el promedio de los 4 exámenes
promedio = (nota1 + nota2 + nota3 + nota4) / 4
print(f"El promedio de los 4 exámenes es: {promedio}")

# Verificar si la cursada está aprobada
if promedio >= 6:
    print("¡Cursada aprobada!")
    # Preguntar por la nota del examen final si la cursada está aprobada
    examen_final = float(input("Ingrese la nota del examen final: "))
    
    # Verificar si el alumno aprobó el examen final
    if examen_final >= 6:
        print("¡Materia aprobada!")
    else:
        print("No aprobó el final de la materia, puede rendir recuperatorio.")
else:
    print("Cursada no aprobada. El alumno no puede rendir el examen final.")
