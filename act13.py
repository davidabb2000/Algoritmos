def act13():
    print("============================================================")
    print("Actividad 13")
    print("============================================================")
    try:

        n1 = float(input("Ingrese la primera nota: "))
        n2 = float(input("Ingrese la segunda nota: "))
        n3 = float(input("Ingrese la tercera nota: "))

        nfinal = (n1 + n2 + n3) / 3

        if nfinal >= 3.0:
            print("La nota final es de:", nfinal, ", El usuario APROBO")
            
        else:
            print("La nota final es de:", nfinal, ", El usuario NO APROBO")
            
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act13()
