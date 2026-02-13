def act4():
    print("============================================================")
    print("Actividad 4")
    print("============================================================")
    try:


        horast = float(input("Ingrese el número de horas trabajadas: "))
        valorh = float(input("Ingrese el valor por hora: "))

        totalsemanal = horast * valorh

        print("El total semanal a pagar es: ", totalsemanal)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act4()
