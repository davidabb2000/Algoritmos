from datetime import datetime

nac = int(input("Ingrese año de nacimiento: "))

fecha_actual = datetime.now()
anio_actual = fecha_actual.year

edad = anio_actual - nac

print("Su edad actual es: ", edad)