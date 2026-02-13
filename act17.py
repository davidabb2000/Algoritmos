def act17():
    print("============================================================")
    print("Actividad 17")
    print("============================================================")
    try:
        from datetime import datetime

        nac = int(input("Ingrese año de nacimiento: "))

        fecha_actual = datetime.now()
        anio_actual = fecha_actual.year

        edad = anio_actual - nac

        print("Su edad actual es: ", edad)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act17()
