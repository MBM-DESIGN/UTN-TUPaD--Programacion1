# Práctico 8: Manejo de archivos.

# Objetivo: Comprender y aplicar el uso de archivos de texto en Python, desarrollando un
# pequeño programa que lea, procese y almacene información sobre productos de manera persistente.
# Manipular datos a través de estructuras como listas y diccionarios, integrando lectura, escritura y buenas prácticas con archivos.

# Resultados del aprendizaje:
# 1.Lectura y escritura de archivos:leer y escribir información en archivos de texto mediante ejemplos prácticos, 
# reconociendo los modos 'r', 'w' y 'a'.
# 2.Manejo de estructuras de datos:convertir líneas de texto en listas y diccionarios, y manipular esta información en memoria
# de forma eficiente.
# 3.Persistencia y reutilización de datos:entender el concepto de persistencia de datos y ser capaz de actualizar archivos 
# sin borrar la información previa, reutilizando y modificando registros.
# 4.Buenas prácticas al trabajar con archivos:aplicar el uso de with open() para el manejo correcto de archivos y 
# validará situaciones comunes como evitar sobrescritura accidental o errores de apertura.

# El programa permite:leer archivo,procesar datos,mostrar o actualizar información y guardar los cambios.
# Primero ejecuto este script para crear el archivo:productos.txt

# Importamos os para que el script pueda interactuar con el sistema de archivos 
# y verificar la presencia del archivo de datos antes de intentar leerlo,
# evitando que el programa intente abrir un archivo inexistente y lance un error.
import os 

# Como no había restricciones en este trabajo para utilizar variables globales,lo hice así porque da mayor claridad al código.
FILENAME = "productos.txt" #define una constante que almacena el nombre del archivo con el que trabajará todo el programa.

# Esta función crea el archivo:productos.txt con los 3 productos iniciales,sólo si el archivo no existe.
def crear_archivo_inicial_si_no_existe(ruta):
    if not os.path.exists(ruta):
        contenido = [
            "Lapicera,120.5,30\n",
            "Cuaderno,350.0,15\n",
            "Regla,80.0,50\n"
        ]
        with open(ruta, "w", encoding="utf-8") as f:
            f.writelines(contenido)
        print(f"Archivo {ruta} creado con 3 productos iniciales.")
    else:
        print(f"Archivo {ruta} ya existe. Se mantiene su contenido.")

# Esta función devuelve una lista de líneas limpias del archivo.Si no existe el archivo, devuelve una lista vacía.
def leer_lineas(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]

# Esta función convierte:nombre,precio,cantidad en un diccionario y los ubica en ese orden por posición.
def linea_a_producto(linea):
    partes = [p.strip() for p in linea.split(",")]
    if len(partes) != 3:
        raise ValueError(f"Línea con formato incorrecto: {linea}") #lanza ValueError si hay algún problema de formato.
    nombre = partes[0]
    precio = float(partes[1])
    cantidad = int(partes[2])
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

# Esta función lee el archivo y devuelve una lista de diccionarios con los productos, sus precios y cantidades.
def cargar_productos(ruta):
    lineas = leer_lineas(ruta)
    productos = []
    for linea in lineas:
        try: #con try except manejamos los errores.
            prod = linea_a_producto(linea)
            productos.append(prod)
        except ValueError as e:
            print("Advertencia:", e)
    return productos

# Esta función muestra la lista de productos en el formato pedido(nombre, precio y cantidad).
def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Esta función agrega("a"de append) una línea al final del archivo sin borrar lo existente.
def agregar_producto_a_archivo(ruta, producto):
    linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(linea)

# Esta función sobrescribe el archivo con la lista completa de productos.
def guardar_todos_los_productos(ruta, productos):
    with open(ruta, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

# Esta función pide nombre, precio y cantidad,hace una validación mínima y devuelve el diccionario.
def pedir_producto_por_teclado():
    nombre = input("Ingrese nombre del producto: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    precio_str = input("Ingrese precio (entero o decimal con .): ").strip()
    cantidad_str = input("Ingrese cantidad (entero): ").strip()
    try:
        precio = float(precio_str)
        cantidad = int(cantidad_str)
    except ValueError:
        raise ValueError("Precio o cantidad con formato inválido.")
    if precio < 0 or cantidad < 0:
        raise ValueError("Precio y cantidad deben ser números positivos.")
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

# Esta función busca por nombre exacto (case insensitive) y devuelve el producto o None.
def buscar_producto(productos, nombre_buscar):
    nombre_norm = nombre_buscar.strip().lower()
    for p in productos:
        if p["nombre"].strip().lower() == nombre_norm:
            return p
    return None

# Consignas 1 y 4:leer y cargar los productos en la lista de diccionarios.
def main():
    productos = cargar_productos(FILENAME)

    # Consigna 2:mostrar productos.
    print("\nProductos actuales:")
    mostrar_productos(productos)

    # Consigna 3:agregar uno o varios productos (se agrega/n como append al archivo y a la lista).
    respuesta = input("\n¿Desea agregar un nuevo producto? (s para sí / n para no): ").strip().lower()
    if respuesta == "s":
        try:
            nuevo = pedir_producto_por_teclado()
            agregar_producto_a_archivo(FILENAME, nuevo)  #persiste inmediatamente.
            productos.append(nuevo)  #mantiene la sincronía en memoria.
            print("Producto agregado correctamente al archivo.")
        except ValueError as e:
            print("No se pudo agregar el producto:", e)
    if respuesta == "n":
        print("No se agregarán productos entonces.")
    else:
        print("Error: debe ingresar una opción válida.") 

    # Consigna 5:buscar producto por nombre.
    buscar = input("\nIngrese el nombre del producto a buscar: ").strip()
    if buscar:
        encontrado = buscar_producto(productos, buscar)
        if encontrado:
            print("Producto encontrado:")
            print(f"Nombre: {encontrado['nombre']}")
            print(f"Precio: ${encontrado['precio']}")
            print(f"Cantidad: {encontrado['cantidad']}")
        else:
            print("Error: el producto no existe.")

    # Consigna 6:guardar productos actualizados sobrescribiendo el archivo.
    respuesta_guardar = input("\n¿Desea guardar todos los productos desde la lista (sobrescribir archivo)? (s/n): ").strip().lower()
    if respuesta_guardar == "s":
        guardar_todos_los_productos(FILENAME, productos)
        print("Archivo sobrescrito con los productos actuales de la lista.")
    else:
        print("No se sobrescribió el archivo.Los cambios que ya se agregaron por append permanecen.")

# Comprueba si el archivo python se está ejecutando directamente(como programa principal) o si se está importando desde otro módulo. 
# Si la condición es verdadera(como en este caso),se ejecuta el bloque indentado:main().
if __name__ == "__main__":
    main()
