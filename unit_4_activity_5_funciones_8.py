# 📌 Consigna: 
# Desarrollar un programa controlado por un menú de opciones generado desde una función llamada menu(), 
# invocada desde el algoritmo principal, y el cual cuenta con las siguientes opciones:  
# 
# - Opción 1 – Adivina el número secreto: por medio de una función llamada adivina() generar un número secreto al azar comprendido en el intervalo [0, 50] y determinar si un número entero y positivo n ingresado por el usuario es igual al número secreto generado por la computadora. La función recibe como argumento el número n ingresado y devuelve como valor de retorno una bandera que indica si el número n es igual al número secreto. Antes de salir de la opción informar con un mensaje en pantalla si el usuario ganó o no ganó el juego.  
# - Opción 2 – Capicúas en el intervalo: dado un intervalo cerrado [desdehasta], ingresado por el usuario, determinar por medio de una función llamada esCapicua(), todos los números capicúas contenidos en el intervalo y mostrarlos. La función recibe como argumentos los extremos desde-hasta del intervalo ingresados por el usuario. Antes de llamar a la función se deberá validar que los extremos del intervalo sean positivos y que el extremo del intervalo desde no sea mayor que el extremo del intervalo hasta.
# - Opción 3 – Salir.
# 
# Nota: puedes intentar combinarlo con el ejercicio de la actividad 6. En este caso solo deberías permitir el acceso al menú cuando se ingrese la contraseña correcta dentro de la cantidad permitida de intentos.

import random

PASSWORD_CORRECTA = "supersecreta_156"
MAX_INTENTOS = 3


# Recibe los intentos ya realizados y el máximo permitido.
# Devuelve True si todavía quedan intentos, False si se agotaron.
def valida_intento(intentos_realizados, max_intentos):
    return intentos_realizados < max_intentos


# Recibe la contraseña ingresada y devuelve True si coincide con la correcta.
def valida_pass(contrasena):
    return contrasena == PASSWORD_CORRECTA


# Muestra el menú y devuelve la opción elegida por el usuario.
def menu():
    print()
    print("----- MENÚ -----")
    print("1 - Adivina el número secreto")
    print("2 - Capicúas en el intervalo")
    print("3 - Salir")
    return int(input("Elija una opción: "))


# Genera un número secreto al azar en [0, 50] y lo compara con n.
# Devuelve True si n es igual al secreto, False si no.
def adivina(n):
    secreto = random.randint(0, 50)
    print(f"El número secreto generado fue: {secreto}")
    return n == secreto


# Recibe un número y devuelve True si es capicúa (se lee igual al derecho y al revés).
def numero_es_capicua(numero):
    original = numero
    invertido = 0
    aux = numero
    while aux > 0:
        invertido = invertido * 10 + aux % 10
        aux = aux // 10
    return original == invertido


# Recibe los extremos del intervalo y muestra todos los capicúas contenidos en [desde, hasta].
def esCapicua(desde, hasta):
    print(f"Números capicúas en el intervalo [{desde}, {hasta}]:")
    hay_capicua = False
    for numero in range(desde, hasta + 1):
        if numero_es_capicua(numero):
            print(numero)
            hay_capicua = True
    if not hay_capicua:
        print("No hay números capicúas en el intervalo.")


# --- Acceso con contraseña (actividad 6) ---
intentos = 0
acceso = False

while valida_intento(intentos, MAX_INTENTOS) and not acceso:
    contrasena = input("Ingrese la contraseña: ")

    if valida_pass(contrasena):
        print("Contraseña correcta")
        acceso = True
    else:
        print("Contraseña incorrecta")
        intentos += 1

# --- Algoritmo principal: menú ---
if not acceso:
    print("Se agotaron los intentos. Acceso denegado.")
else:
    opcion = 0
    while opcion != 3:
        opcion = menu()

        if opcion == 1:
            n = int(input("Ingrese un número entero y positivo: "))
            while n <= 0:
                print("El número debe ser entero y positivo.")
                n = int(input("Ingrese un número entero y positivo: "))

            gano = adivina(n)
            if gano:
                print("Ganaste el juego.")
            else:
                print("No ganaste el juego.")

        elif opcion == 2:
            desde = int(input("Ingrese el extremo desde del intervalo: "))
            hasta = int(input("Ingrese el extremo hasta del intervalo: "))

            while desde <= 0 or hasta <= 0 or desde > hasta:
                print("Los extremos deben ser positivos y desde no puede ser mayor que hasta.")
                desde = int(input("Ingrese el extremo desde del intervalo: "))
                hasta = int(input("Ingrese el extremo hasta del intervalo: "))

            esCapicua(desde, hasta)

        elif opcion == 3:
            print("Fin del programa.")

        else:
            print("Opción no válida. Intente de nuevo.")
