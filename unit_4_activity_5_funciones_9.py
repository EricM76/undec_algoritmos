# 📌 Consigna:
# 
# Desarrollar un programa que permita procesar una cadena de caracteres. El programa será controlado por un menú de opciones generado desde una función llamada menú(), invocada desde el algoritmo principal y la cual cuenta con las siguientes opciones:  
# 
# - Opción 1 – Leer una cadena: permite ingresar una cadena de caracteres desde el teclado. 
#   Desarrollar una función llamada leeCadena() que no reciba ningún argumento y devuelva una cadena de 
#   caracteres leída desde el teclado.  
# - Opción 2 – Contar minúsculas: permite contar la cantidad de letras minúsculas de la cadena de 
#   caracteres ingresada con la opción 1. Para los conteos se deben incluir: letras consonantes minúsculas,
#   vocales minúsculas sin acentuar y acentuadas con tilde ortográfico ‘´’). La opción se debe implementar 
#   por medio de una función llamada cuentaMin().  
# - Opción 3 – Contar consonantes: permite contar la cantidad de letras consonantes de la cadena de caracteres
#   ingresada con la opción 1. La opción se debe implementar por medio de una función llamada 
#   cuentaConsonantes().  
# - Opción 4 – Contar números: permite contar la cantidad de caracteres numéricos de la cadena de
#   caracteres ingresada con la opción 1. El conteo debe incluir los caracteres numéricos del ‘0’ al ‘9’.
#   La opción se debe implementar por medio de una función llamada cuentaNumeros().  
# - Opción 5 – Contar carácter: permite contar la cantidad de veces que aparece un carácter dentro de la
#   cadena ingresada con la opción 1. El carácter a contar será ingresado por el usuario. La opción se debe
#   implementar por medio de una función llamada cuentaCaracter().
# - Opción 6 - Salir. 

MINUSCULAS = "abcdefghijklmnñopqrstuvwxyzáéíóú"
CONSONANTES = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
NUMEROS = "0123456789"


# Muestra el menú y devuelve la opción elegida por el usuario.
def menu():
    print()
    print("----- MENÚ -----")
    print("1 - Leer una cadena")
    print("2 - Contar minúsculas")
    print("3 - Contar consonantes")
    print("4 - Contar números")
    print("5 - Contar carácter")
    print("6 - Salir")
    return int(input("Elija una opción: "))


# No recibe argumentos. Lee y devuelve una cadena ingresada por teclado.
def leeCadena():
    return input("Ingrese una cadena de caracteres: ")


# Recibe la cadena y cuenta letras minúsculas:
# consonantes, vocales sin acento y vocales con tilde (á, é, í, ó, ú).
def cuentaMin(cadena):
    cantidad = 0
    for caracter in cadena:
        if caracter in MINUSCULAS:
            cantidad += 1
    return cantidad


# Recibe la cadena y cuenta las letras consonantes (mayúsculas y minúsculas).
def cuentaConsonantes(cadena):
    cantidad = 0
    for caracter in cadena:
        if caracter in CONSONANTES:
            cantidad += 1
    return cantidad


# Recibe la cadena y cuenta los caracteres numéricos del '0' al '9'.
def cuentaNumeros(cadena):
    cantidad = 0
    for caracter in cadena:
        if caracter in NUMEROS:
            cantidad += 1
    return cantidad


# Recibe la cadena y el carácter a buscar. Devuelve cuántas veces aparece.
def cuentaCaracter(cadena, caracter):
    cantidad = 0
    for c in cadena:
        if c == caracter:
            cantidad += 1
    return cantidad


# --- Algoritmo principal ---
cadena = ""
leida = False
opcion = 0

while opcion != 6:
    opcion = menu()

    if opcion == 1:
        cadena = leeCadena()
        leida = True
        print(f"Cadena ingresada: {cadena}")

    elif opcion == 2:
        if not leida:
            print("Primero debe ingresar una cadena con la opción 1.")
        else:
            cantidad = cuentaMin(cadena)
            print(f"Cantidad de letras minúsculas: {cantidad}")

    elif opcion == 3:
        if not leida:
            print("Primero debe ingresar una cadena con la opción 1.")
        else:
            cantidad = cuentaConsonantes(cadena)
            print(f"Cantidad de consonantes: {cantidad}")

    elif opcion == 4:
        if not leida:
            print("Primero debe ingresar una cadena con la opción 1.")
        else:
            cantidad = cuentaNumeros(cadena)
            print(f"Cantidad de caracteres numéricos: {cantidad}")

    elif opcion == 5:
        if not leida:
            print("Primero debe ingresar una cadena con la opción 1.")
        else:
            caracter = input("Ingrese el carácter a contar: ")
            cantidad = cuentaCaracter(cadena, caracter)
            print(f"El carácter '{caracter}' aparece {cantidad} vez/veces.")

    elif opcion == 6:
        print("Fin del programa.")

    else:
        print("Opción no válida. Intente de nuevo.")
