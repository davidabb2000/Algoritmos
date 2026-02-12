num_ventas = int(input("Número de ventas realizadas: "))
ventas = []

for i in range(num_ventas):
    valor = float(input(f"Valor de la venta {i+1}: "))
    ventas.append(valor)

total = sum(ventas)
promedio = total / num_ventas

print("Total vendido:", total)
print("Promedio por venta:", promedio)
