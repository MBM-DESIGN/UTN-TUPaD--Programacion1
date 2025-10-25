# Práctico 6: Funciones.

# Objetivo: Comprender y aplicar el uso de funciones en la programación, desarrollando algoritmos que implementen modularidad,
# reutilización de código y una organización estructurada para resolver problemas.
# Primero defino todas las funciones con def y luego escribo el programa que llamará a esas funciones definidas.

import math #importo este módulo para poder acceder a funciones matemáticas avanzadas.

# 1.Función llamada imprimir_hola_mundo
def imprimir_hola_mundo(): 
    print("Hola Mundo!")  

# 2.Función con saludo personalizado.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3.Función para solicitar información personal.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4.Función para calcular el área y el perímetro de un círculo.
def calcular_area_circulo(radio):
    return math.pi * radio ** 2 #al haber importado el módulo math más arriba, puedo utilizar aquí el nro. Pi.

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio #al haber importado el módulo math más arriba, puedo utilizar aquí el nro. Pi.

# 5.Función para convertir segundos a horas.
def segundos_a_horas(segundos):
    return segundos / 3600

# 6.Función para armar una tabla de multiplicar.
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7.Función de operaciones matemáticas básicas.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida" #para manejar el error de la división por 0.
    return (suma, resta, multiplicacion, division)

# 8.Función para calcular el índice de Masa Corporal(IMC).
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9.Función para convertir de grados celsius a grados fahrenheit.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10.Función para calcular el promedio.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal.
if __name__ == "__main__":
    imprimir_hola_mundo()
    print ("-" * 50)

    nombre = input("\nIngresá tu nombre: ")
    print(saludar_usuario(nombre))
    print ("-" * 50)

    print("\nInformación personal:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print ("-" * 50)

    print("\nCírculo:")
    radio = float(input("Ingresá el radio: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
    print ("-" * 50)

    print("\nConversión de segundos a horas:")
    segundos = int(input("Ingresá los segundos: "))
    print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas.")
    print ("-" * 50)

    print("\nTabla de multiplicar:")
    numero = int(input("Ingresá un número entero preferentemente del 1 al 10: "))
    tabla_multiplicar(numero)
    print ("-" * 50)

    print("\nOperaciones básicas:")
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")
    print ("-" * 50)

    print("\nCálculo de IMC:")
    peso = float(input("Ingresá tu peso (en kg): "))
    altura = float(input("Ingresá tu altura (en m): "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    print ("-" * 50)

    print("\nConversión de temperatura:")
    celsius = float(input("Ingresá una temperatura en grados celsius: "))
    print(f"El equivalente en grados fahrenheit es: {celsius_a_fahrenheit(celsius):.2f} °F")
    print ("-" * 50)

    print("\nPromedio de tres números:")
    a = float(input("Ingresá el número 1: "))
    b = float(input("Ingresá el número 2: "))
    c = float(input("Ingresá el número 3: "))
    print(f"Promedio: {calcular_promedio(a, b, c):.2f}")
    print ("-" * 50)
