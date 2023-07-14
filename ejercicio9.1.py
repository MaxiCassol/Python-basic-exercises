paises = [input("Dime un pais:\n")]

indice = 0
while len(set(paises)) < 4:
    agregado = input('di otro:\n')


    if agregado in paises:
        print("Ese pais ya esta")

    else:
        paises.append(agregado)
    print(f'paises: {sorted(set(paises))}')



