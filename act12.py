def act12():
    print("============================================================")
    print("Actividad 12")
    print("============================================================")
    try:

        valor = int(input("Ingrese el valor e las ventas mensuales: "))

        if valor > 1000000:
            comm = valor * (10 / 100)

        else:
            comm = valor * (5 / 100)
            
            
        print("El valor de la comision es: ", comm)

    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act12()
