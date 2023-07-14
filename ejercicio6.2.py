

class Alumno:
    nombre = "Maxi"
    nota = 9

a = Alumno()

print("Nombre: ", a.nombre)
print("Nota:   ", a.nota)

if Alumno.nota >= 7:
    print("Estado:  Aprobado")
else:
    print("Estado:  No Aprobado")
