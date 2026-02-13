def act1():
    print("============================================================")
    print("Actividad 1")
    print("============================================================")
    try:
        num1 = int(input("Digite el primer número: "))
        num2 = int(input("Digite el segundo número: "))
        num3 = int(input("Digite el tercer número: "))

        # Cálculos
        resultado = num1 + num2 + num3
        promedio = resultado / 3  # Mantener decimales

        # Salidas
        print("El resultado es:", resultado, "y el promedio es:", promedio)
    
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act1()
