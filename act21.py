capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés (%): ")) / 100
periodos = int(input("Ingrese el número de períodos: "))

monto_final = capital * (1 + tasa) ** periodos

print("Monto final:", monto_final)
