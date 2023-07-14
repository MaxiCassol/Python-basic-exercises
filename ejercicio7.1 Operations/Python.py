from Operations import Operaciones as o


def main():
    sum = o.suma(10, 5)
    res = o.resta(10, 5)
    mul = o.multiplicar(10, 5)
    div = o.dividir(10, 5)
    print("Suma: ", sum, "Resta: ", res, "Multiplicacion: ", mul, "Division: ", div)

if __name__ == '__main__':
    main()