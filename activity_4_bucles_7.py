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

numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))

while numero != 0:
    if numero < 0:
        print("Número ingresado no válido")
    else:
        original = numero
        cifras = 0
        invertido = ""  # texto para no perder ceros al invertir (ej: 120 → 021)

        while numero > 0:
            digito = numero % 10          # última cifra (MOD), incluye ceros
            invertido += str(digito)
            numero = numero // 10         # quita la última cifra (DIV)
            cifras += 1

        print(f"El número {original} tiene {cifras} cifra(s)")
        print(f"Invertido: {invertido}")

        if str(original) == invertido:
            print(f"{original} es capicúa")
        else:
            print(f"{original} no es capicúa")

    numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))

