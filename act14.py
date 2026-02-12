"""14. Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva. """


ntalleres = float(input("Ingrese la nota final de los talleres: "))
nparcial = float(input("Ingrese la nota final de los Examen parciales: "))
nfinal = float(input("Ingrese la nota del examen final: "))

notadef = ntalleres * (30 / 100) + nparcial * (30 / 100) + nfinal * (40 / 100)

print("Su nota final es: ", notadef)