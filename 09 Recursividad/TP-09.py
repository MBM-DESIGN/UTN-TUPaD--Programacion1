# Práctico 11: Aplicación de la Recursividad.

# Objetivo: Comprender el uso de recursividad en problemas matemáticos simples.

# Resultados del aprendizaje:
# 1.Comprensión y aplicación de la recursividad: El estudiante será capaz de definir y comprender el concepto de recursividad, 
# identificando los casos base y recursivos en una función recursiva.
# 2.Diseño y desarrollo de algoritmos recursivos: El estudiante será capaz de diseñar funciones recursivas para resolver 
# problemas complejos, descomponiendo el problema en subproblemas más sencillos.
# 3.Resolución de problemas a través de la recursividad: El estudiante será capaz de aplicar la recursividad en la resolución 
# de una variedad de problemas, como la búsqueda en estructuras de datos, el ordenamiento y la generación de estructuras combinatorias.

# Definición de funciones.
# Consigna 1.Función recursiva que calcula el factorial de un nro. para n >= 0.
def factorial(n):
    if n < 0:
        raise ValueError("Factorial: n debe ser un nro. entero no negativo")
    #caso base
    if n == 0 or n == 1:
        return 1
    #paso recursivo
    return n * factorial(n - 1)

# Consigna 2.Función recursiva que calcula el valor de la serie de Fibonacci en la posición indicada.
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci: n debe ser un nro. entero no negativo")
    #caso base
    if n == 0:
        return 0
    if n == 1:
        return 1
    #paso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

# Consigna 3.Función recursiva que calcula la potencia de un nro. base elevado a un exponente para n >= 0.
def potencia(base, exponente):
    if exponente < 0:
        raise ValueError("Potencia: el exponente debe ser un nro. entero no negativo")
    #caso base
    if exponente == 0:
        return 1
    #paso recursivo: base * base^(exponente-1)
    return base * potencia(base, exponente - 1)

# Consigna 4.Función recursiva que recibe un nro. entero positivo en base decimal y devuelva su representación en binario.
def decimal_a_binario(n):
    if n < 0:
        raise ValueError("Decimal_a_binario: n debe ser un nro. entero positivo")
    #caso base
    if n == 0:
        return "0"
    #caso recursivo
    def _rec(k):
        if k == 0:
            return ""
        resto = k % 2
        cociente = k // 2
        return _rec(cociente) + str(resto)
    return _rec(n)

# Consigna 5.Función recursiva que recibe una cadena de texto sin espacios ni tildes y devuelve True si es palíndromo.
def es_palindromo(palabra, inicio=0, fin=None):
    if fin is None:
        fin = len(palabra) - 1
    #caso base:si inicio >= fin ya se verificó toda la palabra.
    if inicio >= fin:
        return True
    #paso recursivo:compara los caracteres en los extremos.
    if palabra[inicio] != palabra[fin]:
        return False
    #llama recursivamente moviendo los índices hacia adentro.
    return es_palindromo(palabra, inicio + 1, fin - 1)

# Consigna 6.Función recursiva que recibe un nro. entero positivo y devuelve la suma de todos sus dígitos.
def suma_digitos(n):
    if n < 0:
        raise ValueError("Suma_digitos: n debe ser un nro. entero positivo")
    #caso base
    if n < 10:
        return n
    #paso recursivo:el último dígito + la suma de los demás.
    return (n % 10) + suma_digitos(n // 10)

# Consigna 7.Función recursiva que recibe el nro. de bloques del nivel más bajo de la pirámide y calcula el total de bloques.
def contar_bloques(n):
    if n < 1:
        raise ValueError("Contar_bloques: n debe ser un nro. entero positivo")
    #caso base
    if n == 1:
        return 1
    #paso recursivo
    return n + contar_bloques(n - 1)

# Consigna 8.Función recursiva que recibe un nro., un dígito y devuelve cuántas veces aparece ese dígito en el nro.
def contar_digito(numero, digito):
    if numero < 0:
        raise ValueError("Contar_digito: debe ser un nro. entero positivo")
    if not (0 <= digito <= 9):
        raise ValueError("Contar_digito: el digito elegido debe estar entre 0 y 9")
    #caso base
    if numero == 0:
        return 1 if digito == 0 else 0
    #paso recursivo:comparar el último dígito y avanzar con el cociente.
    def _rec(n):
        if n == 0:
            return 0
        cuenta_actual = 1 if (n % 10) == digito else 0
        return cuenta_actual + _rec(n // 10)
    return _rec(numero)

# Ejecución de la aplicación.
if __name__ == "__main__":

    print("Ejercicio 1: Factoriales desde 1 hasta el número indicado")
    m = int(input("Ingrese un nro. entero positivo para calcular los factoriales hasta ese número: "))
    for i in range(1, m + 1):
        print(f"{i}! = {factorial(i)}")

    print("\nEjercicio 2: Serie de Fibonacci")
    p = int(input("Ingrese la posición máxima (un nro. entero positivo): "))
    serie = [fibonacci(i) for i in range(p + 1)]
    print("Serie de Fibonacci hasta la posición", p, "->", serie)

    print("\nEjercicio 3: Potencia recursiva")
    b = int(input("Ingrese para la base, un nro. entero positivo: "))
    e = int(input("Ingrese para el exponente, un nro. entero positivo: "))
    print(f"{b}^{e} = {potencia(b, e)}")

    print("\nEjercicio 4: Decimal a binario")
    d = int(input("Ingrese un nro. entero positivo para convertir a binario: "))
    print(f"{d} en binario es {decimal_a_binario(d)}")

    print("\nEjercicio 5: Palíndromo")
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    print(f"es_palindromo('{palabra}') -> {es_palindromo(palabra.lower())}")

    print("\nEjercicio 6: Suma de dígitos")
    n6 = int(input("Ingrese un nro. entero positivo para sumar sus dígitos: "))
    print(f"suma_digitos({n6}) = {suma_digitos(n6)}")

    print("\nEjercicio 7: Contar bloques de una pirámide")
    n7 = int(input("Ingrese la cantidad de bloques en el nivel más bajo (n >= 1): "))
    print(f"Total bloques para n={n7}: {contar_bloques(n7)}")

    print("\nEjercicio 8: Contar las apariciones de un dígito")
    n8 = int(input("Ingrese un nro. entero positivo: "))
    dig = int(input("Ingrese el dígito a contar (de 0 a 9): "))
    print(f"El dígito {dig} aparece {contar_digito(n8, dig)} veces en {n8}")

