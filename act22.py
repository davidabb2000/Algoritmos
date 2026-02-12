inicial = int(input("Cantidad inicial en inventario: "))
vendido = int(input("Cantidad vendida: "))
recibido = int(input("Cantidad recibida: "))

final = inicial - vendido + recibido

print("Inventario final:", final)
