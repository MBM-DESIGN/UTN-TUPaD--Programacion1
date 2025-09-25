# Práctico 5: Listas.

# Objetivo: Desarrollar la comprensión y la capacidad de manipular listas en Python mediante la aplicación
#de conceptos fundamentales como la indexación, la modificación de elementos, el uso de
#métodos integrados y el manejo de listas anidadas.

# 1.Programa para crear una lista con las notas de 10 estudiantes.
# Creo la lista de notas.
notas = [8, 5, 10, 7, 6, 9, 4, 8, 10, 6]

# Muestro la lista completa usando un bucle for.
print("Lista de notas:")
for nota in notas:
    print(nota, end=" ") #end=" " las muestra en una línea

# Calculo y muestro el promedio.
suma_notas = sum(notas)
promedio = suma_notas / len(notas)
print(f"\n\nPromedio de las notas: {promedio}")

# Indico la nota más alta y la más baja.
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print(f"La nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")
print ("-" * 50)

# 2.Programa para pedir al usuario que cargue 5 productos en una lista.
# Pido al usuario que cargue 5 productos.
productos = []
print("\nIngresá 5 productos para la lista de compras:")
for i in range(5):
    producto = input(f"Producto {i + 1}: ")
    productos.append(producto)

# Muestro la lista ordenada alfabéticamente.
print("\nLista de productos ordenada:")
for producto in sorted(productos):
    print(f"- {producto}")

# Pregunto al usuario qué producto desea eliminar.
producto_a_eliminar = input("\n¿Qué producto deseás eliminar de la lista?: ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"\nSe ha eliminado '{producto_a_eliminar}'. Lista actualizada:")
    for producto in productos:
        print(f"- {producto}")
else:
    print(f"El producto '{producto_a_eliminar}' no estaba en la lista.")
print ("-" * 50)

# 3.Programa para generar una lista con 15 números enteros al azar entre 1 y 100.
import random

# Genero 15 números enteros al azar entre 1 y 100.
numeros_azar = []
for _ in range(15):
    numeros_azar.append(random.randint(1, 100))

print("\nLista de números generados al azar:")
for numero in numeros_azar:
    print(numero, end=" ")

# Creo las listas para pares e impares.
pares = []
impares = []

for numero in numeros_azar:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Muestro los resultados.
print("\n\nLista de números pares:")
for par in pares:
    print(par, end=" ")
print(f"\nTotal de números pares: {len(pares)}")

print("\nLista de números impares:")
for impar in impares:
    print(impar, end=" ")
print(f"\nTotal de números impares: {len(impares)}")
print ("-" * 50)

# 4.Programa para trabajar con una lista de elementos repetidos.
# Lista original con valores repetidos.
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Creo una nueva lista sin los elementos repetidos.
sin_repetidos = []
for item in datos:
    if item not in sin_repetidos:
        sin_repetidos.append(item)

# Muestro el resultado.
print("\nLista original:", end=" ")
for d in datos:
    print(d, end=" ")

print("\nLista sin elementos repetidos:", end=" ")
for s in sin_repetidos:
    print(s, end=" ")
print() # Salto de línea final
print ("-" * 50)

# 5.Programa para crear una lista con los nombres de 8 estudiantes presentes en clase.
# Muestro la lista inicial de estudiantes.
presentes = ["Ana", "Juan", "Maria", "Carlos", "Sofia", "Luis", "Elena", "Pedro"]

print("\nLista de estudiantes presentes:")
for estudiante in presentes:
    print(f"- {estudiante}")

# Pregunto al usuario la acción que quiere realizar.
accion = input("\n¿Querés agregar (A) un nuevo estudiante o eliminar (E) uno existente?: ").upper()

if accion == 'A':
    nuevo_estudiante = input("Ingresá el nombre del nuevo estudiante: ")
    presentes.append(nuevo_estudiante)
    print(f"'{nuevo_estudiante}' ha sido agregado.")
elif accion == 'E':
    estudiante_a_eliminar = input("Ingresá el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in presentes:
        presentes.remove(estudiante_a_eliminar)
        print(f"'{estudiante_a_eliminar}' ha sido eliminado.")
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Opción no válida.")

# Muestro la lista final.
print("\nLista final de estudiantes:")
for estudiante in presentes:
    print(f"- {estudiante}")
print ("-" * 50)

# 6.Programa para dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).
# Muestro la lista original con 7 números.
numeros = [10, 20, 30, 40, 50, 60, 70]

print("\nLista original:")
for n in numeros:
    print(n, end=" ")

# Roto los elementos una posición a la derecha.
if numeros: # Me aseguro de que la lista no esté vacía.
    ultimo_elemento = numeros.pop() # Esto saca el último elemento y
    numeros.insert(0, ultimo_elemento) # lo inserta al principio.

print("\nLista rotada:")
for n in numeros:
    print(n, end=" ")
print()
print ("-" * 50)

# 7.Programa para crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# Matriz 7x2: 7 días de la semana, 2 temperaturas diarias (la mínima y la máxima).
temperaturas = [[18, 25], [12, 23], [12, 20], [14, 22], [18, 28], [18, 29], [19, 29]]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Calculo los promedios.
total_minimas = 0
total_maximas = 0
for dia in temperaturas:
    total_minimas += dia[0]
    total_maximas += dia[1]

promedio_minimas = total_minimas / len(temperaturas)
promedio_maximas = total_maximas / len(temperaturas)

print(f"\nPromedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")

# Calculo el día con mayor amplitud térmica.
mayor_amplitud = 0
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

print(f"El día con mayor amplitud térmica fue el {dia_mayor_amplitud} con {mayor_amplitud}°C.")
print ("-" * 50)

# 8.Programa para crear una matriz con las notas de 5 estudiantes en 3 materias.
# Matriz 5x3: 5 estudiantes, 3 materias.
notas = [
    [9, 7, 8],   # Estudiante 1
    [10, 6, 7],   # Estudiante 2
    [5, 9, 10], # Estudiante 3
    [6, 8, 9],   # Estudiante 4
    [6, 7, 6]    # Estudiante 5
]
materias = ["Programación", "AySO", "Matemática"]

# Muestro el promedio de cada estudiante.
print("\nPromedio por estudiante:")
for i in range(len(notas)):
    promedio_estudiante = sum(notas[i]) / len(notas[i])
    print(f" - Estudiante {i + 1}: {promedio_estudiante:.2f}")

# Muestro el promedio de cada materia.
print("\nPromedio por materia:")
for j in range(len(materias)): # Itera sobre las columnas (materias).
    suma_materia = 0
    for i in range(len(notas)): # Itera sobre las filas (estudiantes).
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f" - {materias[j]}: {promedio_materia:.2f}")
print ("-" * 50)

# 9.Programa para representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializo el tablero 3x3 con guiones representando casillas vacías.
tablero = [["-" for _ in range(3)] for _ in range(3)]
turno = "X"
jugadas = 0

print("\n¡Juego de Ta-Te-Ti!")

while jugadas < 9:
    # Para mostrar el tablero.
    print("\nTablero actual:")
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()

    # Para pedir la jugada.
    print(f"\nTurno del jugador '{turno}'")
    try:
        fila = int(input("Ingrese fila (1-3): ")) - 1
        columna = int(input("Ingrese columna (1-3): ")) - 1

        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == "-":
            tablero[fila][columna] = turno
            jugadas += 1
            # Para cambiar de turno.
            if turno == "X":
                turno = "O"
            else:
                turno = "X"
        else:
            print("Posición inválida u ocupada. Intente de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")

print("\nJuego terminado. Tablero final:")
for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print()
print ("-" * 50)

# 10.Programa para mostrar una tienda que registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Matriz 4x7: 4 productos, 7 días.
ventas = [
    [10, 20, 15, 5, 25, 30, 12],  # Producto 1
    [5, 15, 10, 2, 20, 25, 8],   # Producto 2
    [20, 30, 25, 10, 35, 40, 22], # Producto 3
    [8, 18, 12, 7, 28, 32, 15]   # Producto 4
]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Para mostrar total vendido por producto (sumo las filas).
print("\nTotal de ventas por producto:")
totales_por_producto = []
for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    totales_por_producto.append(total_producto)
    print(f"- Producto {i + 1}: {total_producto} unidades")

# Para mostrar el día con mayores ventas totales (sumo las columnas).
ventas_por_dia = [0] * 7 # [0, 0, 0, 0, 0, 0, 0]
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        ventas_por_dia[j] += ventas[i][j]

max_ventas_dia = max(ventas_por_dia)
indice_mejor_dia = ventas_por_dia.index(max_ventas_dia)
mejor_dia = dias_semana[indice_mejor_dia]
print(f"\nEl día con mayores ventas fue el {mejor_dia} con {max_ventas_dia} unidades.")

# Para indicar cuál fue el producto más vendido.
producto_mas_vendido = max(totales_por_producto)
indice_mas_vendido = totales_por_producto.index(producto_mas_vendido)
print(f"El producto más vendido en la semana fue el Producto {indice_mas_vendido + 1}.")
print ("-" * 50)

