def act14():
    print("============================================================")
    print("Actividad 14")
    print("============================================================")
    try:
        ntalleres = float(input("Ingrese la nota final de los talleres: "))
        nparcial = float(input("Ingrese la nota final de los Examen parciales: "))
        nfinal = float(input("Ingrese la nota del examen final: "))

        notadef = ntalleres * (30 / 100) + nparcial * (30 / 100) + nfinal * (40 / 100)

        print("Su nota final es: ", notadef)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act14()
