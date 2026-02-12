"""15. Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales."""

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n2 < n1:
    print("El primer numero es mayor que el segundo")
elif n1 == n2:
    print("Los numeros son iguales")
else:
    print("El segundo numero es mayor que el primero")

