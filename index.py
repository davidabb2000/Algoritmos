

import os
import sys
import subprocess

while True:
    print("============================================================")
    print("Algoritmos basicos de python")
    print("Por David Alejandro Barrientos Bedoya")
    print("Menu principal")
    print("============================================================")
    
    for i in range(1, 26):
        print(f"{i}. Ejecutar Algoritmo")
    print("0. SALIR \n")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "0":
        print("Saliendo... ")
        break
    
    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"act{opcion}.py"
        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print("No existe")
    
    else:
        print("Opcion no valida")
    
    input("\n Presiona ENTER para continuar...")
    
