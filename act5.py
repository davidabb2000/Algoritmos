horast = float(input("Ingrese el número de horas trabajadas: "))
valorh = float(input("Ingrese el valor por hora: "))

if horast > 40:
    horasad = horast - 40
    salariototal = (40 * valorh) + (horasad * valorh * 1.5)

else:
    salariototal = valorh * horast
    
print("El salario total es: ", salariototal)