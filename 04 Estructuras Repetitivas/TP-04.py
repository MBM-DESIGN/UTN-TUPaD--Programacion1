# Práctico 4: Estructuras repetitivas.

# Objetivo: Implementar ciclos para resolver problemas que requieran repetición de acciones.

# 1.Programa para mostrar nros. enteros desde 0 hasta 100(incluyendo ambos extremos), en orden creciente,
#  mostrando un número por línea.

# Bucle 'for' para iterar sobre la secuencia de números.
for numero in range(101): # La función 'range(101)' genera una secuencia que comienza en 0
    print(numero)         # y termina en 100 (el límite superior 101 no se incluye).

print ("-" * 50)

# 2.Programa para calcular y mostrar en pantalla la cantidad de dígitos que contiene un nro. entero.

# El bloque 'try-except' asegura que el programa no falle
# si el usuario ingresa algo que no es un número entero (como texto).
try:
    numero_usuario = input("Por favor, ingresa un número entero: ")     # La función input() siempre devuelve el dato como una cadena de texto.
    numero = int(numero_usuario)    # Intentamos convertir la cadena de texto a un número entero.

    if numero == 0:     # El bucle no funcionaría para el 0, así que lo manejamos por separado.
        cantidad_digitos = 1
    else:
        cantidad_digitos = 0    # Creamos un contador que empezará en 0.
        numero = abs(numero)    # Usamos el valor absoluto (función abs) para que el bucle funcione igual para nros. positivos y negativos.
        
        while numero > 0:        
            numero = numero // 10   # La división entera por 10 remueve el último dígito del número.
            cantidad_digitos += 1 # Por cada último dígito que "eliminamos" en cada vuelta, incrementamos nuestro contador en 1.

    print(f"El número {numero_usuario} tiene {cantidad_digitos} dígito(s).") # Mostramos el resultado final al usuario.

except ValueError:
    print("Error: El número ingresado no es un entero válido. Por favor, intentá de nuevo.") # Se ejecuta si el usuario no ingresa un nro. entero.

print ("-" * 50)

# 3.Programa para calcular la suma de todos los nros. enteros que se encuentran en un rango, sin incluir los números ingresados.

try:
    num1 = int(input("Ingresá el primer número entero: "))
    num2 = int(input("Ingresá el segundo número entero: "))

    inicio = min(num1, num2) # La función min() devuelve el menor de los dos, y max() el mayor.
    fin = max(num1, num2) # Así identificamos cuál es el menor y el mayor para ordenar el rango.

    suma_total = 0 # Inicializamos la variable para almacenar la suma.

    for numero in range(inicio + 1, fin): # La función 'range(inicio + 1, fin)' genera una secuencia que comienza con el nro. min y termina en el nro. max.
        # En cada vuelta, añadimos el número actual a nuestro acumulador (suma_total).
        suma_total += numero  # Esto es una simplificación de: suma_total = suma_total + numero
    print(f"La suma de los números enteros entre {inicio} y {fin} es: {suma_total}") # Así logramos que nos muestre los números elegidos en orden ascendente.

except ValueError:
    print("Error: ambos valores deben ser números enteros válidos.") # Se ejecuta si el usuario no ingresa un nro. entero.

print ("-" * 50)

# 4.Programa para sumar nros. enteros de forma continua, con un ciclo que se detiene cuando el usuario ingresa el nro. 0.

suma_total = 0 # Inicializamos la variable para almacenar la suma acumulada.
while True: # Generamos un bucle infinito que corta (break) cuando el usuario ingresa 0.
    try:
        numero = int(input("Ingresá un número entero (o 0 para terminar): "))

        if numero == 0: # El 0 es la condición de salida del bucle.
            break  # Esta instrucción termina el bucle 'while' inmediatamente.
        # Si el número ingresado no es 0, lo añadimos a nuestro acumulador.
        suma_total += numero  # Esto es una simplificación de: suma_total = suma_total + numero
        print(f"Suma parcial: {suma_total}") # Para mostrar la suma en cada paso.

    except ValueError:
        print("Entrada no válida. Por favor, ingresá solo números enteros.") # Para indicarle al usuario el error.

print ("-" * 50)

print(f"Programa finalizado. La suma total es: {suma_total}") # Esta línea se ejecuta al terminar el bucle (al ingresar 0).

print ("-" * 50)

# 5.Programa para que el usuario adivine un nro. aleatorio entre 0 al 9 y muestre cuántos intentos fueron necesarios.

import random

numero_secreto = random.randint(0, 9) # Para generar un nro. aleatorio entre 0 y 9.

intentos = 0 # Inicializamos el contador de intentos.

print("¡Adivina el número secreto entre 0 y 9!") # Mensaje de bienvenida al usuario.

while True: # Bucle principal del juego.
    numero_usuario = int(input("Ingresá el número secreto: ")) # Pedir número al usuario.
    
    intentos += 1 # Incrementa el contador.
    
    if numero_usuario == numero_secreto:     # Si el usuario adivina,
        print(f"¡Felicitaciones! Adivinaste el número {numero_secreto}")
        print(f"Te tomó {intentos} intentos")
        break # termina el bucle.

print ("-" * 50)

# 6.Programa para imprimir los nros. pares entre 0 y 100 en orden decreciente.

print("Números pares del 100 al 0 en orden decreciente:") # Mensaje del programa.
print("-" * 50)

for numero in range(100, -1, -2): # Bucle que va desde 100 hasta 0 de 2 en 2.
    print(numero)

print("-" * 50)

# 7.Programa para calcular la suma de nros. comprendidos desde el 0 hasta el número que ingresa el usuario.

numero = int(input("Ingresá un número entero positivo: ")) # Pedir al usuario que ingrese un número entero positivo.

suma = 0 # Inicializamos la variable para acumular la suma.

for i in range(numero + 1): # Bucle for para sumar todos los nros. desde 0 hasta el número ingresado por el usuario.
    suma += i

print(f"La suma de los números desde 0 hasta {numero} es: {suma}") # Para mostrar el resultado.

print("-" * 50)

# 8.Programa para contar nros. pares, impares, positivos y negativos.

cantidad = 5  # Cantidad de números a ingresar.

# Inicializamos los contadores.
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresá {cantidad} números enteros:") # Consigna para el usuario.

for i in range(cantidad):  # Bucle para ingresar y analizar los números.
    numero = int(input(f"Número {i + 1}: "))

    if numero % 2 == 0:    # Verificamos si el nro. es par o impar.
        pares += 1
    else:
        impares += 1
    
    if numero > 0:         # Verificamos si el nro. es positivo o negativo.
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- RESULTADOS ---")  # Mostramos los resultados.
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

print("-" * 50)

# 9.Programa para calcular la media (promedio) de nros. enteros.

cantidad_numeros = 5  # Cantidad de números a ingresar.
    
print(f"=== Calculadora de Media ===")
print(f"Ingresá {cantidad_numeros} números enteros:") # Consigna para el usuario.
    
numeros = []  # Lista vacía para almacenar los nros.
    
for i in range(cantidad_numeros):  # Bucle para solicitar los nros. al usuario.
        while True:
            try:
                numero = int(input(f"Número {i + 1}: ")) # {i + 1} toma el valor de i y le suma 1 sucesivamente.
                numeros.append(numero) # .append() agrega el número al final de la lista numeros y cada vez que el bucle se ejecuta, añade un número más a la lista.
                break  # Para salir del bucle si el input es válido.
            except ValueError: # Para informar del error al usuario.
                print("Error: Ingresá un número entero válido.")
    
suma_total = sum(numeros)     # Para calcular la media.
media = suma_total / cantidad_numeros
    
print(f"\n=== Resultados ===") # Mostramos los resultados.
print(f"Números ingresados: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Cantidad de números: {cantidad_numeros}")
print(f"Media: {media:.2f}")

print("-" * 50)

# 10.Programa para invertir el orden de los dígitos de un nro.

print("=== Inversor de Dígitos ===")
    
while True:
        try:
            numero_original = int(input("Ingresá un número entero: "))  # Solicitamos el nro. al usuario.
            break  # Para salir del bucle si el input es válido.
        except ValueError: # Para informar del error al usuario.
            print("Error: Ingresa un número entero válido.")

# Usando strings: Convertimos el número a string para manipular los caracteres.
numero_str = str(abs(numero_original))  # abs() quita el signo negativo si existe.
    
# Invertimos el string usando slicing [::-1].
numero_invertido_str = numero_str[::-1]
    
# Convertimos de vuelta a nro. entero.
numero_invertido = int(numero_invertido_str)
    
# Si el número original era negativo, hacemos negativo el resultado.
if numero_original < 0:
        numero_invertido = -numero_invertido
    
print(f"\n=== Resultados ===") # Mostramos los resultados.
print(f"Número original: {numero_original}")
print(f"Número invertido: {numero_invertido}")

print("-" * 50)
