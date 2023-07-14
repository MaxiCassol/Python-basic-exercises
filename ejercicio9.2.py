from functools import reduce

milista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def miapp(x):
    if x % 2 :
        return True

    return False

def suma(a, b):
    return a + b

resultado = list(filter(miapp, milista))

resultadosuma = reduce(suma, resultado)

print(resultadosuma)