
# Simulador de Carrera de Autos:
# Implementa un programa que simule una carrera de autos entre varios competidores. Cada competidor tiene una velocidad aleatoria y la carrera se desarrolla en rondas. El programa debe mostrar el progreso de la carrera en cada ronda y determinar el ganador al final.

import random
import time

# Parámetros de la carrera
DISTANCIA_META = 100  # Distancia total de la carrera

# Lista de competidores
competidores = ["Auto Rojo", "Auto Azul", "Auto Verde", "Auto Amarillo"]

# Inicializar posiciones
posiciones = {auto: 0 for auto in competidores}

print("🏁 ¡Comienza la carrera! 🏁\n")

# Simulación por rondas
ganador = None
ronda = 1

while not ganador:
    print(f"Ronda {ronda}:")
    for auto in competidores:
        avance = random.randint(1, 10)  # Avance aleatorio por ronda
        posiciones[auto] += avance

        # Mostrar el avance con una barra visual
        barra = "-" * posiciones[auto] + "🚗"
        print(f"{auto:<15}: {barra} ({posiciones[auto]} metros)")

        # Verificar si hay un ganador
        if posiciones[auto] >= DISTANCIA_META and not ganador:
            ganador = auto

    print("-" * 60)
    time.sleep(1)  # Pausa de 1 segundo entre rondas
    ronda += 1

# Mostrar el ganador
print(f"\n🏆 ¡El ganador es {ganador}! 🏆")
