def act25():
    print("============================================================")
    print("Actividad 1")
    print("============================================================")
    try:

        num_ventas = int(input("Número de ventas realizadas: "))
        ventas = []

        for i in range(num_ventas):
            valor = float(input(f"Valor de la venta {i+1}: "))
            ventas.append(valor)

        total = sum(ventas)
        promedio = total / num_ventas

        print("Total vendido:", total)
        print("Promedio por venta:", promedio)
    except ValueError:
        print("Debes ingresar un número válido")

if __name__ == "__main__":
    act25()