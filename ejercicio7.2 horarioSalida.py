import time


def main():
    t = time.strftime("%H", time.localtime())
    print(t, "hs")

    if t >= '19':
        print("Hora de ir a casa!!!")
    else:
        tiemporestante = 19 - int(t)
        print("Horas de trabajo restantes: ", tiemporestante)


if __name__== '__main__':
    main()