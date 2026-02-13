"""16. Número par o impar: Solicitar un número entero e indicar si es par o impar."""
def act16():
    print("============================================================")
    print("Actividad 16")
    print("============================================================")
    try:
        numero = int(input("Ingrese un numero: "))

        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
            
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act16()
