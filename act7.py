def act7():
    print("============================================================")
    print("Actividad 7")
    print("============================================================")
    try:

        valort = int(input("Ingrese el valor total: "))

        if valort > 200000:
            valort = valort * 0.9

        print("El valor total es:", valort)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act7()
