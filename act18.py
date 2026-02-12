"""18. Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor."""

edad = int(input("Ingrese su edad: "))

if edad < 17:
    print("Eres menor de edad")
elif edad > 60:
    print("Eres adulto mayor")
else:
    print("Eres mayor de edad")