def act6():
    print("============================================================")
    print("Actividad 6")
    print("============================================================")
    try:


        namep = str(input("Enter your name: "))
        preciounit = int(input("Enter the price of the product: "))
        cant = int(input("Enter the quantity of the product: "))
        total = preciounit * cant

        print("La cantidad total de", cant, namep, "cada unidad valiendo", preciounit, "es igual a", total)
    
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act6()

