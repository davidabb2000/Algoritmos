"""19. Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario."""
def act19():
    print("============================================================")
    print("Actividad 1")
    print("============================================================")
    try:
        valor = float(input("Ingrese un valor en COP: "))
        usd = 3650

        total = valor / usd

        print("El valor de COP a USD es: ", total)
        
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act19()