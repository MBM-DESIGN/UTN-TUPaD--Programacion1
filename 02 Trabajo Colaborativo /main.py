#TP 1 Secuenciales
#Ejercicio 1
#Creo la carpeta ejercicios con el archivo principal main.py
#Escribo el código y cuando quiero ejecutarlo en la consola, me situo en el archivo y escribo el comando con la version del interprete que va a ejecutar el archivo indicado:
# python3 main.py (lo escribo en la terminal y me sale la leyenda: Hola Mundo!)

saludo = "Hola Mundo!"
print(saludo)

#Ejercicio 2
nombre = input ("Por favor, escribe tu nombre: ")
saludo = f"Hola {nombre}!"
print(saludo)

#Ejercicio 3: no repito el input nombre porque ya viene de arrastre del ejercicio 2
apellido = input ("Por favor, escribe tu apellido: ")
edad = input ("Por favor, escribe tu edad: ")
lugar = input ("Por favor, escribe tu lugar de residencia: ")
saludo = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}"
print(saludo)

#Ejercicio 4: "import math" importo el módulo que me permite utilizar la constante pi y .2f para mostrar sólo 2 decimales del float
import math

radio = float (input ("Por favor ingresá el radio de un círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5:
segundos = int (input ("Por favor ingresá la cantidad de segundos: "))
horas = segundos / 3600
print(f"La cantidad de horas son: {horas:.2f}")

#Ejercicio 6:
numero = int (input ("Por favor ingresá un número para ver su tabla de multiplicar: "))
for i in range(1,11):
    print(f"{numero} X {i} = {numero * i}" )

#Ejercicio 7:
numero1 = int (input ("Por favor ingresá un numero entero distinto de 0: "))
numero2 = int (input ("Por favor ingresá otro numero entero distinto de 0 y del anterior: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"La suma de los números es: {suma}")
print(f"La resta de los números es: {resta}")
print(f"La multiplicación de los números es: {multiplicacion}")
print(f"La división de los números es: {division}")

#Ejercicio 8: el IMC es el índice de masa corporal
peso = float (input ("Por favor ingresá tu peso en kg: "))
altura = float (input ("Por favor ingresá tu altura en metros: "))
IMC = peso / (altura **2)
print(f"Tu IMC es: {IMC:.2f}")

#Ejercicio 9:
celsius = float (input ("Por favor ingresá una temperatura en grados celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La misma temperatura en grados fahrenheit son: {fahrenheit:.2f}°")

#Ejercicio 10:
numero1 = float (input ("Por favor ingresá un primer numero distinto de 0: "))
numero2 = float (input ("Por favor ingresá un segundo numero distinto de 0: "))
numero3 = float (input ("Por favor ingresá un tercer numero distinto de 0: "))
print(f"El promedio de los 3 números ingresados es: {(numero1 + numero2 + numero3)/3:.2f}")