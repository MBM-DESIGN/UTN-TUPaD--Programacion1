# Práctico 3: Estructuras condicionales

# 1.Programa para verificar la mayoría de edad

# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: ")) 
# Verificar si es mayor de 18 años
if edad > 18:
    print("Sos mayor de edad")
print ("-" * 40)

# 2.Programa para evaluar si una nota está aprobada

# Solicitar la nota al usuario
nota = int(input("Por favor, ingresa tu nota (en número entero): "))
# Evaluar si está aprobada o desaprobada
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print ("-" * 40)

# 3.Programa para verificar números pares usando el operador de módulo (%)

# Solicitar un número al usuario
numero = int(input("Por favor, ingresa un número: "))
# Verificar si el número es par usando el operador de módulo
if numero % 2 == 0:
    print("Has ingresado un número par")
else:
    print("Por favor, ingresá un número par")
print ("-" * 40)

# 4.Programa para clasificar a las personas por categorías de edad

# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))
# Clasificar por categorías usando if-elif-else
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
print ("-" * 40)

# 5.Programa para validar la longitud de una contraseña usando la función len()

# Solicitar la contraseña al usuario
contraseña = input("Por favor, ingresá una contraseña (que contenga entre 8 y 14 caracteres): ")
# Validar la longitud usando la función len()
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Has ingresado una contraseña correcta")
else:
    print("Por favor, ingresá una contraseña entre 8 y 14 caracteres")
print ("-" * 40)

# 6.Programa con parámetros estadísticos de: moda (mode), mediana (median) y media (mean); para predecir el patrón de distribución

# Importar las librerías necesarias
import random
from statistics import mode, median, mean
# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Calcular las medidas estadísticas
try:
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    # Mostrar los valores calculados
    print("Números aleatorios generados:", numeros_aleatorios)
    print(f"\nMedidas estadísticas:")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    # Determinar el tipo de sesgo
    print(f"\nAnálisis del sesgo:")
    if media > mediana > moda:
        print("Resultado: Sesgo positivo o a la derecha")
        print("(Media > Mediana > Moda)")
    elif media < mediana < moda:
        print("Resultado: Sesgo negativo o a la izquierda")
        print("(Media < Mediana < Moda)")
    elif media == mediana == moda:
        print("Resultado: Sin sesgo")
        print("(Media = Mediana = Moda)")
    else:
        print("Resultado: Distribución sin un patrón de sesgo claro")
        print("(No cumple exactamente con los criterios de sesgo definidos)")
except Exception as e:
    print(f"Error al calcular las medidas estadísticas: {e}")
    print("Esto puede deberse a:")
    print("- No hay valores repetidos (problema con la moda)")
    print("- Lista vacía o con datos inválidos")
print ("-" * 40)

# 7.Programa que añade el signo de exclamación si el string termina en vocal

# Solicitar una frase o palabra al usuario
texto = input("Por favor, ingresá una frase o palabra: ")
# Definir las vocales (incluye mayúsculas y minúsculas)
vocales = "aeiouAEIOU"
# Verificar si el texto termina en vocal
if len(texto) > 0 and texto[-1] in vocales:
    # Si termina en vocal, añadir un signo de exclamación al final
    texto_resultado = texto + "!"
    print(texto_resultado)
else:
    # Si no termina en vocal, imprimir lo ingresado tal como está
    print(texto)
print ("-" * 40)

# 8.Programa para transformar nombres usando las funciones: upper(), lower() y title()

# Solicitar el nombre al usuario
nombre = input("Por favor, ingresá tu nombre: ")
# Mostrar las opciones disponibles
print("\nSeleccioná una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")  
print("3. Nombre con primera letra mayúscula")
# Solicitar la opción deseada
opcion = input("\nIngresá el número de opción (1, 2 o 3): ")
# Transformar el nombre según la opción seleccionada
if opcion == "1":
    nombre_transformado = nombre.upper()
    print(f"\nResultado: {nombre_transformado}")
elif opcion == "2":
    nombre_transformado = nombre.lower()
    print(f"\nResultado: {nombre_transformado}")
elif opcion == "3":
    nombre_transformado = nombre.title()
    print(f"\nResultado: {nombre_transformado}")
else:
    print("\nOpción no válida. Por favor, seleccioná 1, 2 o 3.")
print ("-" * 40)

# 9.Programa para clasificar terremotos según la escala de Richter

# Pedir al usuario la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Clasificar según la escala de Richter
if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"
# Imprimir el resultado
print(f"Clasificación: {clasificacion}")
print ("-" * 40)

# 10.Programa para determinar la estación del año

# Le pedimos al usuario que ingrese su hemisferio, el mes y el día.
# Usamos .upper() para convertir la letra del hemisferio a mayúscula y evitar errores.
# Usamos int() para convertir el mes y el día a números enteros.
print("¡Averigüemos en qué estación del año estás!")
hemisferio = input("¿En qué hemisferio te encontrás? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresá el número del mes actual (por ejemplo, 9 para septiembre): "))
dia = int(input("Ingresa el día actual: "))
# Creamos una variable para guardar la estación y la dejamos vacía.
estacion = ""
# Usamos estructuras condicionales para ver en qué rango de fechas estamos.
# Primer rango: del 21 de diciembre al 20 de marzo.
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == 'N':
        estacion = "Invierno ❄️"
    elif hemisferio == 'S':
        estacion = "Verano ☀️"
# Segundo rango: del 21 de marzo al 20 de junio.
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == 'N':
        estacion = "Primavera 🌸"
    elif hemisferio == 'S':
        estacion = "Otoño 🍂"
# Tercer rango: del 21 de junio al 20 de septiembre.
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == 'N':
        estacion = "Verano ☀️"
    elif hemisferio == 'S':
        estacion = "Invierno ❄️"
# Cuarto rango: del 21 de septiembre al 20 de diciembre.
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == 'N':
        estacion = "Otoño 🍂"
    elif hemisferio == 'S':
        estacion = "Primavera 🌸"
# Si la variable 'estacion' tiene un valor, lo imprimimos por pantalla.
# Si no, es porque el usuario ingresó datos incorrectos.
if estacion:
    print(f"\n¡Según los datos que ingresaste, te encuentras en {estacion} !")
else:
    print("\nLos datos ingresados no son correctos. Por favor, intenta de nuevo.")
print ("-" * 40)

