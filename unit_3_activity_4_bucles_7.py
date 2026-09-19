# 📌 Consigna:
# Diseñar un programa que permita ingresar una serie de números enteros positivos,
# cuente la cantidad de cifras de cada uno y determine si el número es capicúa o no. 
# La carga de datos finaliza cuando el usuario ingresa un cero (0). 
# Recordemos que un número es capicúa cuando se lee igual de derecha a izquierda y 
# de izquierda a derecha, es decir, el número ingresado es igual a su invertido. 
# Por ejemplo, si consideramos el número 7631 podemos concluir que no es capicúa ya que no es igual 
# a su invertido 1367. 
# En otro ejemplo, considerando el número 2882 podemos concluir que es capicúa ya que es igual a su
# invertido 2882.
# 
# También recordemos el uso de los operadores // (DIV) y % (MOD) en la descomposición de números 
# usando sus valores posicionales:
# - // (DIV) para obtener el cociente de la división.
# - % (MOD) para obtener el resto de la división.

# Pedimos el primer número. Si es 0, el while no entra y el programa termina
numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))

# El 0 es la marca de fin: mientras no se ingrese, seguimos procesando números
while numero != 0:
    # Los negativos no se analizan; se pide otro número al final del while
    if numero < 0:
        print("Número ingresado no válido")
    else:
        # Guardamos una copia: "numero" se va a ir destrozando al sacarle cifras
        original = numero
        cifras = 0
        # Texto (no int) para no perder ceros al invertir (ej: 120 → "021")
        invertido = ""

        # Descomposición posicional: sacamos una cifra por vuelta hasta que quede 0
        while numero > 0:
            # % 10 (MOD) = última cifra. Ej: 7631 % 10 → 1
            digito = numero % 10
            invertido += str(digito)  # la vamos pegando de atrás hacia adelante
            # // 10 (DIV) = quita esa última cifra. Ej: 7631 // 10 → 763
            numero = numero // 10
            cifras += 1

        print(f"El número {original} tiene {cifras} cifra(s)")
        print(f"Invertido: {invertido}")

        # Es capicúa si se lee igual de izquierda a derecha que al revés
        if str(original) == invertido:
            print(f"{original} es capicúa")
        else:
            print(f"{original} no es capicúa")

    # Pedimos el siguiente número (o 0 para cortar). Va al final para no repetir el input
    numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))

