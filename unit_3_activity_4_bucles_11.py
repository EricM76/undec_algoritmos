# 📌 Consigna:
# Desarrollar un programa controlado por un Menú de Opciones:
# 
# Opción 1 – Números del 1 al 50
# - La opción debe mostrar los números comprendidos en el intervalo [1-50] de adelante hacia atrás y de atrás 
#   hacia adelante y calcular la suma de los números impares.
# 
# Opción 2 – Divisores propios
# - La opción debe determinar los divisores propios de un número n y mostrar la suma de los mismos en pantalla. 
# - Los divisores propios de un número natural n son los números naturales comprendidos entre 1 y n-1 que lo 
#   pueden dividir, resultando como cociente entre ellos  otro número natural y de resto 0, es decir, 
#   la división es exacta. 
# - Cada número tiene una cantidad concreta de divisores. Por ejemplo, los divisores de 12 son: 1, 2, 3, 4, 6 y 12; 
#   sin embargo, los divisores propios de 12 son todos sus divisores sin considerar el propio número, ósea 
#   1, 2, 3, 4 y 6. En otro ejemplo, los divisores propios de 28 son 1, 2, 4, 7 y 14. 
# - Validar que el número n ingresado sea positivo.
# 
# Opción 3 – Números primos
# - La opción debe permitir determinar si un número ingresado es primo o no. Decimos que un número primo n es un 
#   número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1. Por ejemplo, el 
#   número 3 es primo, ya que tiene solamente dos divisores, el 1 y el 3. Por otro lado, 12 no es primo, ya que
#   además de 1 y 12, tiene también a los siguientes divisores 2, 3, 4, 6. 
# - Validar que el número n ingresado sea positivo.
# 
# Opción 4 –Números perfectos
# - La opción debe determinar si un número ingresado es o no es perfecto. Se dice que un número n es perfecto si 
#   la suma de sus divisores propios es igual al número n ingresado. Por ejemplo, para determinar si el número 12 
#   es un número perfecto, sólo tenemos en cuenta sus divisores propios: 1, 2, 3, 4 y 6. Si hacemos la sumatoria
#   de los divisores propios de 12:
#   1+ 2 + 3+ 4 + 6 = 16 != 12
#   Por lo tanto, el número 12 no es un número perfecto. En otro ejemplo, 28 es un número perfecto, pues sus 
#   divisores propios son 1, 2, 4, 7 y 14, que suman 28. Otros ejemplos de números perfectos son los números 496, 
#   8128. 
# - Validar que el número n ingresado sea positivo.
# 
# Opción 5 –Números amigos
# - La opción debe determinar si dos números ingresados n y m son amigos. Dos números son amigos si la sumatoria 
#   de los divisores propios del primer número n es igual al segundo número m, y viceversa. Por ejemplo, 
#   los divisores propios del número 284, son 1, 2, 4, 71 y 142, cuya suma es 1 + 2 + 4 + 71 + 142 = 220.
#   Si ahora buscamos los divisores propios del número obtenido 220 estos son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 
#   110 y la suma de estos es 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284, precisamente el primer 
#   número analizado. Por este motivo, se dice que los números 220 y 284 son números amigos.
# - Otros ejemplos de números amigos son (1184, 1210), (17 296, 18 416) y (9 363 584, 9 437 056).
# - Validar que los números n y m ingresados sean positivos.
# 
# Opción 6 - Salir

# El 6 es la marca de salida: mientras no se elija, el menú se vuelve a mostrar
opcion = 0
while opcion != 6:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1 - Números del 1 al 50")
    print("2 - Divisores propios")
    print("3 - Números primos")
    print("4 - Números perfectos")
    print("5 - Números amigos")
    print("6 - Salir")

    opcion = int(input("Ingrese una opción: "))

    # ----- Opción 1: intervalo [1-50] en ambos sentidos y suma de impares -----
    if opcion == 1:
        adelante = ""
        atras = ""
        suma_impares = 0

        # Un solo recorrido alcanza para armar las dos listas y sumar los impares
        for numero in range(1, 51):
            adelante += str(numero) + " "
            # El de atrás se va pegando al frente: 1, luego 2 1, luego 3 2 1, ...
            atras = str(numero) + " " + atras

            # Impar: el resto de dividir por 2 no es 0
            if numero % 2 != 0:
                suma_impares += numero

        print("\nNúmeros de adelante hacia atrás:")
        print(adelante)
        print("Números de atrás hacia adelante:")
        print(atras)
        print(f"Suma de los números impares: {suma_impares}")

    # ----- Opción 2: divisores propios de n y su suma -----
    elif opcion == 2:
        n = int(input("Ingrese un número positivo: "))
        # 0 y los negativos no son naturales positivos; se pide de nuevo
        while n <= 0:
            print("Número ingresado no válido")
            n = int(input("Ingrese un número positivo: "))

        divisores = ""
        suma_divisores = 0

        # Los propios van de 1 a n-1 (el propio n no se cuenta)
        for divisor in range(1, n):
            # Si el resto es 0, la división es exacta: es divisor
            if n % divisor == 0:
                divisores += str(divisor) + " "
                suma_divisores += divisor

        if suma_divisores == 0:
            # El 1 no tiene divisores propios: el rango (1, 1) no entra al for
            print(f"El número {n} no tiene divisores propios")
        else:
            print(f"Divisores propios de {n}: {divisores}")
            print(f"Suma de los divisores propios: {suma_divisores}")

    # ----- Opción 3: ¿es primo? -----
    elif opcion == 3:
        n = int(input("Ingrese un número positivo: "))
        while n <= 0:
            print("Número ingresado no válido")
            n = int(input("Ingrese un número positivo: "))

        # Por definición, 1 no es primo (necesita exactamente dos divisores: 1 y él mismo)
        if n == 1:
            print("El número 1 no es primo")
        else:
            es_primo = True
            # Buscamos algún divisor entre 2 y n-1. Si aparece uno, ya no es primo
            for divisor in range(2, n):
                if n % divisor == 0:
                    es_primo = False

            if es_primo:
                print(f"El número {n} es primo")
            else:
                print(f"El número {n} no es primo")

    # ----- Opción 4: ¿es perfecto? (suma de propios == n) -----
    elif opcion == 4:
        n = int(input("Ingrese un número positivo: "))
        while n <= 0:
            print("Número ingresado no válido")
            n = int(input("Ingrese un número positivo: "))

        suma_divisores = 0
        for divisor in range(1, n):
            if n % divisor == 0:
                suma_divisores += divisor

        # Ej: 28 → 1+2+4+7+14 = 28 (perfecto). 12 → 16 != 12 (no lo es)
        if suma_divisores == n:
            print(f"El número {n} es perfecto")
        else:
            print(f"El número {n} no es perfecto (suma de divisores propios: {suma_divisores})")

    # ----- Opción 5: ¿n y m son amigos? -----
    elif opcion == 5:
        n = int(input("Ingrese el primer número positivo: "))
        while n <= 0:
            print("Número ingresado no válido")
            n = int(input("Ingrese el primer número positivo: "))

        m = int(input("Ingrese el segundo número positivo: "))
        while m <= 0:
            print("Número ingresado no válido")
            m = int(input("Ingrese el segundo número positivo: "))

        # Suma de los divisores propios de n
        suma_n = 0
        for divisor in range(1, n):
            if n % divisor == 0:
                suma_n += divisor

        # Suma de los divisores propios de m
        suma_m = 0
        for divisor in range(1, m):
            if m % divisor == 0:
                suma_m += divisor

        print(f"Suma de los divisores propios de {n}: {suma_n}")
        print(f"Suma de los divisores propios de {m}: {suma_m}")

        # Son amigos si cada suma da el otro número (ej: 220 y 284)
        if suma_n == m and suma_m == n:
            print(f"{n} y {m} son números amigos")
        else:
            print(f"{n} y {m} no son números amigos")

    elif opcion == 6:
        print("Programa finalizado")

    else:
        print("Opción ingresada no válida")
