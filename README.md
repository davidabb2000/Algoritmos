---------------------------------
Autor: David Barrientos
Aprendiz - Desarrollo de software
----------------------------------------------

📘 Algoritmos – Actividad 1
Este repositorio contiene ejercicios básicos de programación en Python, diseñados para practicar estructuras de control, manejo de errores y operaciones aritméticas.

📂 Descripción
El archivo act1.py solicita al usuario ingresar tres números enteros, realiza la suma de ellos y calcula el promedio. El programa incluye manejo de excepciones para garantizar que el usuario ingrese valores válidos.

⚙️ Funcionamiento
El programa pide al usuario tres números enteros mediante la función input().

Convierte los valores a enteros (int()).

Calcula:

Resultado: la suma de los tres números.

Promedio: la media aritmética de los tres números.

Muestra los resultados en pantalla.

Si el usuario ingresa un valor no numérico, se captura la excepción ValueError y se muestra un mensaje de error.

🖥️ Ejemplo de uso
bash
$ python act1.py
Digite el primer número: 10
Digite el segundo número: 20
Digite el tercer número: 30
El resultado es: 60 y el promedio es: 20.0
📌 Características
Manejo de errores con try/except.

Promedio calculado con división estándar para conservar decimales.

Estructura modular: la función act1() se ejecuta solo si el archivo se corre directamente (if __name__ == "__main__":).

🚀 Próximas mejoras
Validar entradas con bucles para que el usuario vuelva a intentar si se equivoca.

Usar f-strings para mejorar la presentación de resultados.

Ampliar el programa para incluir otras operaciones matemáticas (máximo, mínimo, etc.).
