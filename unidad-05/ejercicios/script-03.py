
# Calculadora de Propina:
# Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta en un restaurante. El programa debe calcular automáticamente diferentes opciones de propinas (por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina.

# Función para calcular la propina
def calcular_propina(total, porcentaje):
    return total * (porcentaje / 100)

# Función principal del programa
def calculadora_propina():
    # Solicitar al usuario el total de la cuenta
    while True:
        try:
            total = float(input("Ingresa el total de la cuenta en el restaurante: $"))
            if total < 0:
                print("El total debe ser un número positivo. Intenta nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el total de la cuenta.")

    # Definir los porcentajes de propina
    porcentajes = [15, 18, 20]

    # Calcular y mostrar las opciones de propinas y el monto total a pagar
    print("\nOpciones de propina:")
    for porcentaje in porcentajes:
        propina = calcular_propina(total, porcentaje)
        total_a_pagar = total + propina
        print(f"Propina del {porcentaje}%: ${propina:.2f}")
        print(f"Total a pagar con propina del {porcentaje}%: ${total_a_pagar:.2f}")
        print("-" * 40)

# Llamar a la función principal
calculadora_propina()
