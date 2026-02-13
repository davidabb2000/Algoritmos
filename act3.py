def act3():
    print("============================================================")
    print("Actividad 3")
    print("============================================================")
    try:
        tempc = float(input("Ingrese la temperatura en grados Celsius: "))
        tempf = (tempc * 9/5) + 32


        print("La temperatura en grados Fahrenheit es:", tempf) 
    
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act3()
