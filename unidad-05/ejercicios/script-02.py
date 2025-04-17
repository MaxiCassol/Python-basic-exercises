
# Lista de Tareas Pendientes:
# Crea un programa que permita al usuario mantener una lista de tareas pendientes. El programa debe permitir agregar tareas nuevas, marcar tareas como completadas y mostrar la lista actualizada de tareas.

# Lista de tareas pendientes
tareas = []

# Función para mostrar la lista de tareas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Lista de Tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i}. {tarea['tarea']} - {estado}")

# Bucle principal del programa
while True:
    print("\nMenu de Tareas:")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar lista de tareas")
    print("4. Salir")

    # Solicitar la opción
    opcion = input("Elige una opción (1-4): ")

    # Opción 1: Agregar nueva tarea
    if opcion == '1':
        tarea = input("Escribe la nueva tarea: ")
        tareas.append({"tarea": tarea, "completada": False})
        print("Tarea agregada exitosamente.")

    # Opción 2: Marcar tarea como completada
    elif opcion == '2':
        mostrar_tareas()
        try:
            tarea_id = int(input("Ingresa el número de la tarea que has completado: "))
            if 1 <= tarea_id <= len(tareas):
                tareas[tarea_id - 1]['completada'] = True
                print(f"Tarea '{tareas[tarea_id - 1]['tarea']}' marcada como completada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor ingresa un número válido.")

    # Opción 3: Mostrar lista de tareas
    elif opcion == '3':
        mostrar_tareas()

    # Opción 4: Salir
    elif opcion == '4':
        print("Saliendo del programa.")
        break

    # Opción inválida
    else:
        print("Opción no válida. Por favor elige entre 1 y 4.")
