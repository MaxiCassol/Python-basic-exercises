
# Gestor de Inventario de Tienda:
# Crea un sistema simple de gestión de inventario para una tienda. El programa debe permitir agregar productos nuevos, actualizar la cantidad disponible de un producto y mostrar la lista actualizada de productos en stock.

# Gestor de Inventario de Tienda

inventario = {}

def mostrar_menu():
    print("""
Gestor de Inventario

1. Agregar nuevo producto
2. Actualizar cantidad de producto
3. Mostrar inventario
4. Salir
""")

def agregar_producto():
    producto = input("Nombre del producto a agregar: ").lower()
    if producto in inventario:
        print("Ese producto ya existe en el inventario.")
    else:
        cantidad = int(input("Cantidad inicial: "))
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

def actualizar_cantidad():
    producto = input("Producto a actualizar: ").lower()
    if producto in inventario:
        cantidad = int(input("Nueva cantidad a agregar (puede ser negativa): "))
        inventario[producto] += cantidad
        print(f"Ahora hay {inventario[producto]} unidades de '{producto}'.")
    else:
        print("Ese producto no existe en el inventario.")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"- {producto.capitalize()}: {cantidad} unidades")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_cantidad()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
