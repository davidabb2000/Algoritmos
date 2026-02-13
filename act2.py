# 2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
def act2():
    print("============================================================")
    print("Actividad 2")
    print("============================================================")
    try:
        base = float(input("Digite la base del rectángulo: "))
        altura = float(input("Digite la altura del rectángulo: "))

        area = base * altura

        print("El área del rectángulo es:", area)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act2()
