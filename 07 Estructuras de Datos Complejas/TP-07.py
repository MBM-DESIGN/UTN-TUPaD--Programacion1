# Práctico 6: Estructuras de datos complejas.

# Objetivo: Dominar el uso de estructuras de datos complejas en Python para almacenar, organizar y manipular datos 
# de manera eficiente, aplicando buenas prácticas y optimizando el rendimiento de las aplicaciones.

# Resultados del aprendizaje:
# 1.Comprender y aplicar iterables: listas, tuplas y sets.
# 2.Introducirnos a estructuras de datos complejas: diccionarios.

# Primero defino todas las funciones con def luego escribo el programa principal y ejecuto las funciones ya definidas.

# Para asegurar que:
# El usuario solo pueda ingresar datos alfabéticos válidos(sin números ni símbolos) en los inputs así requeridos.
# El usuario solo pueda ingresar datos numéricos válidos(sin letras ni símbolos)en los inputs así requeridos.
# El programa evite guardar y mostrar datos duplicados.
# Utilicé:
# isalpha() para asegurarnos que cada nombre tenga solo letras.
# isdigit() para asegurarnos que la hora tenga solo números enteros.
# .lower() para normalizar los nombres y evitar duplicados por mayúscula como "María" vs "maria".
# .capitalize() para mejorar la presentación de los nombres en pantalla al convertir la primera letra en mayúscula y el resto 
# en minúscula, especialmente si fueron ingresados en minúscula.

# 1.Añadimos frutas al diccionario: las frutas son las claves y sus precios los valores relacionados con esas claves.
def agregar_frutas(precios):
    precios.update({
        'Naranja': 1200,
        'Manzana': 1500,
        'Pera': 2300
    })

# 2.Actualizamos los precios del diccionario.
def actualizar_precios(precios):
    precios['Banana'] = 1330
    precios['Manzana'] = 1700
    precios['Melón'] = 2800

# 3.Creamos una lista de frutas (sin los precios).
def obtener_lista_frutas(precios):
    return list(precios.keys()) #retornamos las claves: keys(nombres de las frutas) pero sin sus valores: values(precios).

# 4.Creamos un programa de agenda telefónica que permita almacenar y consultar contactos(keys: claves) y números(values: valores).
def agenda_telefonica():
    contactos = {} #utilizamos un diccionario para almacenar pares nombre–número
    for _ in range(5): #el guión bajo es una convención cuando no necesitamos usar la variable del bucle.
        #usamos range(5) para repetir el bloque 5 veces como dice la consigna y permitirle al usuario cargar 5 contactos.
        # Validamos que el nombre ingresado contenga sólo letras.
        while True:
            nombre = input("Ingresá el nombre del contacto a almacenar: ").strip().lower()
            if nombre.isalpha():
                break
            else:
                print("El nombre debe contener sólo letras.Intentá de nuevo.")
        # Validamos que el número ingresado contenga sólo caracteres numéricos.
        while True:
            numero = input("Ingresá el número telefónico del contacto: ").strip()
            if numero.isdigit():
                break
            else:
                print("El número debe contener sólo dígitos numéricos.Intentá de nuevo.")

        contactos[nombre] = numero

    # Consultamos el contacto(sin distinguir mayúsculas/minúsculas).
    consulta = input("\nIngresá el nombre del contacto que querés consultar: ").strip().lower()
    if consulta in contactos:
        print(f"{consulta.capitalize()}: {contactos[consulta]}")
    else:
        print("Contacto no encontrado.")

# 5.Solicitamos al usuario una frase e imprimimos: palabras únicas(()set) y frecuencia({}diccionario).
def analizar_frase():
    frase = input("Escribí una frase: ").lower()
    palabras = frase.split()
    palabras_unicas = set(palabras)
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    print("Palabras únicas:", palabras_unicas)
    print("Frecuencia de palabras:", frecuencia)

# 6.Para encontrar el promedio de 3 alumnos, creamos 1 tupla de 3 notas.
def promedios_alumnos():
    alumnos = {} #utilizamos un diccionario para almacenar las tuplas de notas.
    for _ in range(3): #el guión bajo es una convención cuando no necesitamos usar la variable del bucle.
#usamos range(3) para repetir el bloque 3 veces como dice la consigna y permitirle al usuario cargar los nombres de 3 alumnos.
        # Validamos que en el campo nobre, el usuario ingrese sólo letras.
        while True:
            nombre = input("Ingresá el nombre del/a alumno/a: ").strip().lower()
            if nombre.isalpha():
                break
            else:
                print("El nombre debe contener sólo letras.Intentá de nuevo.")
        # Validamos que las 3 notas ingresadas sean numéricas.
        notas = []
        for i in range(3): #el guión bajo es una convención cuando no necesitamos usar la variable del bucle.
#usamos range(3) para repetir el bloque 3 veces como dice la consigna y permitirle al usuario cargar las notas de 3 alumnos.
            while True:
                nota = input(f"Ingresá la nota {i+1} de {nombre.capitalize()}: ").strip()
                try:
                    if nota.replace('.', '', 1).isdigit():
                        notas.append(float(nota))
                        break
                    else:
                        print("La nota debe ser un número válido.Intentá de nuevo.")
                except ValueError:
                    print("Error al convertir la nota.Intentá de nuevo.")

        alumnos[nombre] = tuple(notas)

    # Mostramos los promedios.
    print("\nPromedios de los alumnos:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre.capitalize()}: promedio = {promedio:.2f}")                

# 7.Armamos 2 sets representando los datos del parcial 1 y del parcial 2.
def analizar_aprobados():
    def ingresar_nombres(parcial_num):
        while True:
            print(f"Ingresá los nombres de quienes aprobaron el parcial {parcial_num} (separados por coma):")
            entrada = input("➡ Ejemplo: Ana, Luis, María\n> ")
            nombres = [nombre.strip().lower() for nombre in entrada.split(",")]
            # Validamos que todos los nombres sean de caracteres alfabéticos.
            if all(nombre.isalpha() for nombre in nombres):
                return set(nombres)
            else:
                print("Los nombres deben contener solo letras.Intentá de nuevo.")

# Validamos los ingresos de ambos parciales.
    parcial1 = ingresar_nombres(1)
    parcial2 = ingresar_nombres(2)

# Operaciones de conjuntos(sets).
# Estudiantes que aprobaron ambos parciales(intersección: quién está en ambos conjuntos).
    ambos = parcial1 & parcial2        #analizamos la intersección (&) de ambos sets.

# Estudiantes que aprobaron solo uno de los dos parciales(diferencia simétrica: quién está en uno solo).
    uno_solo = (parcial1 ^ parcial2)   #analizamos la diferencia simétrica (^) entre ambos sets.

# Estudiantes que aprobaron al menos un parcial(unión sin repetidos: todos los que están en al menos uno).
    al_menos_uno = parcial1 | parcial2 #analizamos la unión (|) de los 2 sets.

# Resultados de las operaciones de conjuntos(sets).
    print("Aprobados en ambos parciales:", sorted(nombre.capitalize() for nombre in ambos))
    print("Aprobados en un solo parcial:", sorted(nombre.capitalize() for nombre in uno_solo))
    print("Total de aprobados (sin repetir nombres):", sorted(nombre.capitalize() for nombre in al_menos_uno))

# 8.Armamos un diccionario(claves: nombres de los productos y valores:stock) para la gestión de stock.
# El programa permitirá consultar el stock de 1 producto, agregar unidades de stock e incorporar un nuevo producto.
def gestion_stock():
    # Diccionario con nombres normalizados en minúsculas como claves
    stock = {'arroz': 10, 'fideos': 5}

    # Validamos que el nombre del producto sea sólo de letras.
    while True:
        producto = input("Ingresá el nombre del producto a consultar: ").strip().lower()
        if producto.isalpha():
            break
        else:
            print("El nombre del producto debe contener sólo letras.Intentá de nuevo.")

    # Si el producto ya existe en el stock
    if producto in stock:
        print(f"Stock actual de {producto.capitalize()}: {stock[producto]}")
        # Validamos que la cantidad a agregar sea numérica.
        while True:
            agregar = input("¿Cuántas unidades deseás agregar?: ").strip()
            if agregar.isdigit():
                stock[producto] += int(agregar)
                break
            else:
                print("La cantidad agregar debe ser un número entero positivo.Intentá de nuevo.")
    else:
        # Si se trata de un producto nuevo: validamos la cantidad inicial.
        while True:
            nuevo_stock = input("Producto nuevo.¿Cuántas unidades deseás agregar?: ").strip()
            if nuevo_stock.isdigit():
                stock[producto] = int(nuevo_stock)
                break
            else:
                print("La cantidad agregar debe ser un número entero positivo.Intentá de nuevo.")

    # Mostramos el estado final del stock con los nombres capitalizados.
    print("Estado final del stock:")
    for nombre, cantidad in stock.items():
        print(f"🔹 {nombre.capitalize()}: {cantidad}")

# 9.Armamos una agenda(que permita consultar qué actividad hay en cierto día y hora) con tuplas(claves:día,hora 
# y valores:eventos).
def agenda_eventos():
    # Diccionario con claves normalizadas: día en minúsculas, hora como string de dos dígitos.
    agenda = {
        ('lunes', '10'): 'Reunión de equipo',
        ('martes', '14'): 'Clase de Python'
    }
    # Validamos que el input día sólo contenga letras.
    while True:
        dia = input("Ingresá el día: ").strip().lower()
        if dia.isalpha():
            break
        else:
            print("El día debe contener solo letras.Intentá de nuevo.")
    # Validamos que el input hora sólo contenga dígitos numéricos.
    while True:
        hora = input("Ingresá la hora (por ejemplo: 10, 14): ").strip()
        if hora.isdigit():
            break
        else:
            print("La hora debe contener solo números.Intentá de nuevo.")

    # Consultamos un evento.
    evento = agenda.get((dia, hora), "No hay actividad registrada.")
    print(f"Actividad para {dia.capitalize()} a las {hora}: {evento}")

# 10.Armamos un diccionario invertido de países-capitales.
def invertir_diccionario(paises_capitales):
    return {capital: pais for pais, capital in paises_capitales.items()}

# Consignas: 1, 2 y 3. Programa principal de frutas: llamado a las funciones.
if __name__ == "__main__":
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    agregar_frutas(precios_frutas)
    actualizar_precios(precios_frutas)
    print("Lista de frutas:", obtener_lista_frutas(precios_frutas))
    print ("-" * 50)

# Consigna 4. Programa de agenda telefónica: ejecutamos la función.
    agenda_telefonica()
    print ("-" * 50)

# Consigna 5. Programa de palabras únicas y frecuencias de palabras: ejecutamos la función.
    analizar_frase()
    print ("-" * 50)

# Consigna 6. Programa de promedio de alumnos: ejecutamos la función.
    promedios_alumnos()
    print ("-" * 50)

# Consigna 7. Programa para analizar aprobados de 2 parciales: ejecutamos la función.
    analizar_aprobados()
    print ("-" * 50)

# Consigna 8. Programa de gestión de stock: ejecutamos la función.
    gestion_stock()
    print ("-" * 50)

# Consigna 9. Programa de agenda de eventos: ejecutamos la función.
    agenda_eventos()
    print ("-" * 50)

# Consigna 10. Programa de diccionario de países-capitales invertido: llamamos a la función y le pasamos el diccionario(sin invertir)
# como argumento para que lo invierta.
    print(invertir_diccionario({'Argentina': 'Buenos Aires', 'Francia': 'París'}))
    print ("-" * 50)    


