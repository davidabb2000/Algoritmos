peso = float(input("Ingrese el peso del paquete (kg): "))

if peso <= 5:
    costo = 10000
else:
    costo = 20000

print("Valor del envío:", costo)
