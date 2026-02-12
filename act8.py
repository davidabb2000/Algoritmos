precio = int(input("Ingrese el precio del producto: "))
pdescuento = float(input("Ingrese el descuento: "))

descuento = precio * (pdescuento / 100)
preciof = precio - descuento

print("El precio final es: ", preciof) 