valor = int(input("Ingrese el valor e las ventas mensuales: "))

if valor > 1000000:
    comm = valor * (10 / 100)

else:
    comm = valor * (5 / 100)
    
    
print("El valor de la comision es: ", comm)