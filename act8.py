def act8():
    print("============================================================")
    print("Actividad 8")
    print("============================================================")
    try:

        precio = int(input("Ingrese el precio del producto: "))
        pdescuento = float(input("Ingrese el descuento: "))

        descuento = precio * (pdescuento / 100)
        preciof = precio - descuento

        print("El precio final es: ", preciof) 
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act8()
