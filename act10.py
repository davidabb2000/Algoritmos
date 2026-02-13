def act10():
    print("============================================================")
    print("Actividad 10")
    print("============================================================")
    try:

        prods = int(input("Ingrese la cantidad de productos comprados: "))
        valor = float(input("Ingrese el valor de cada producto: "))

        valort = prods * valor

        print("El valor total es: ", valort)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act10()
