def act5():
    print("============================================================")
    print("Actividad 5")
    print("============================================================")
    try:

        horast = float(input("Ingrese el número de horas trabajadas: "))
        valorh = float(input("Ingrese el valor por hora: "))

        if horast > 40:
            horasad = horast - 40
            salariototal = (40 * valorh) + (horasad * valorh * 1.5)

        else:
            salariototal = valorh * horast
            
        print("El salario total es: ", salariototal)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act5()
