def act11():
    print("============================================================")
    print("Actividad 11")
    print("============================================================")
    try:

        valor = float(input("Ingrese el valor total de ventas del vendedor: "))

        comm = valor * (5 / 100)

        print("El vendedor debe recibir: ", comm)

    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act11()
