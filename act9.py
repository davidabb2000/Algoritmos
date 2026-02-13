def act9():
    print("============================================================")
    print("Actividad 9")
    print("============================================================")
    try:

        valor = int(input("Ingresa el valor de la venta:"))

        iva = valor * (19 / 100)
        valort = valor + iva

        print("El valor del IVA es: ", iva)

        print("El valor total es: ", valort)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act9()
