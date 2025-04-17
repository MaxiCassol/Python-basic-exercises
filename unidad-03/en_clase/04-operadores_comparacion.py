# Operadores de comparación en Python

# Operador de igualdad (==)
print("Operador de igualdad (==)")
print("¿5 es igual a 5?", 5 == 5)  # True
print("¿5 es igual a 3?", 5 == 3)  # False
print("¿'abc' es igual a 'abc'?", "abc" == "abc")  # True
print("¿'ABC' es igual a 'abc'?", "ABC" == "abc")  # False
print("--------------------")

# Operador de desigualdad (!=)
print("Operador de desigualdad (!=)")
print("¿5 es diferente de 3?", 5 != 3)  # True
print("¿5 es diferente de 5?", 5 != 5)  # False
print("¿'abc' es diferente de 'ABC'?", "abc" != "ABC")  # True
print("--------------------")

# Operador de mayor que (>)
print("Operador de mayor que (>)")
print("¿5 es mayor que 3?", 5 > 3)  # True
print("¿3 es mayor que 5?", 3 > 5)  # False
print("¿'b' es mayor que 'a'?", "b" > "a")  # True (orden alfabético)
print("--------------------")

# Operador de menor que (<)
print("Operador de menor que (<)")
print("¿3 es menor que 5?", 3 < 5)  # True
print("¿5 es menor que 3?", 5 < 3)  # False
print("¿'a' es menor que 'b'?", "a" < "b")  # True (orden alfabético)
print("--------------------")

# Operador de mayor o igual que (>=)
print("Operador de mayor o igual que (>=)")
print("¿5 es mayor o igual a 5?", 5 >= 5)  # True
print("¿5 es mayor o igual a 3?", 5 >= 3)  # True
print("¿3 es mayor o igual a 5?", 3 >= 5)  # False
print("--------------------")

# Operador de menor o igual que (<=)
print("Operador de menor o igual que (<=)")
print("¿3 es menor o igual a 5?", 3 <= 5)  # True
print("¿5 es menor o igual a 5?", 5 <= 5)  # True
print("¿5 es menor o igual a 3?", 5 <= 3)  # False
print("--------------------")

# Ejemplo práctico: Comparación combinada con operadores aritméticos
print("Ejemplo práctico: Comparación combinada")
resultado = (2 + 3) > 4  # Primero se realiza la suma (2 + 3 = 5), luego la comparación (5 > 4)
print("¿2 + 3 es mayor que 4?", resultado)  # True
print("--------------------")