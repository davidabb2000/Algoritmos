capital = float(input("Ingrese el capital: "))
tasa = float(input("Ingrese la tasa de interés (%): ")) / 100
tiempo = int(input("Ingrese el tiempo en meses: "))

interes = capital * tasa * tiempo
total = capital + interes

print("Interés simple:", interes)
print("Valor total a pagar:", total)
