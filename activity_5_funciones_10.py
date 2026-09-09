# 📌 Consigna:
#
# Simule un juego de lotería para 5 jugadores. Cada jugador ingresará el número para su jugada por medio 
# de una función llamada jugada(), el número ingresado debe estar comprendido en el intervalo [0, 100]. 
# Luego de ingresar todas las jugadas, el programa debe simular el juego a través de una función llamada 
# lotería(). Ésta función genera al azar un número aleatorio, también comprendido en el intervalo [0, 100], 
# y determina si hubo algún ganador entre los 5 jugadores (o más de uno) informado la situación con un mensaje 
# en pantalla.
# 
# Nota: en Python, podrá definir las variables correspondientes como globales o aprovechar la característica 
# propia de Python que permite devolver más de un valor de retorno.

import random

NUMEROS_JUGADORES = 5
NUMERO_MAXIMO = 100


# Recibe el número ingresado por el jugador y devuelve True si está en [0, 100], False si no.
def validaJugada(numero):
    if 0 <= numero <= NUMERO_MAXIMO:
        return True
    else:
        print(f"Número no válido. Debe estar entre 0 y {NUMERO_MAXIMO}.")
        return False


# Pide el número de un jugador, lo valida y lo devuelve cuando está en [0, 100].
def jugada(numero_jugador):
    numero = int(input(f"Jugador {numero_jugador}, ingrese su número [{0}, {NUMERO_MAXIMO}]: "))
    valida = validaJugada(numero)

    while not valida:
        numero = int(input(f"Jugador {numero_jugador}, ingrese su número [{0}, {NUMERO_MAXIMO}]: "))
        valida = validaJugada(numero)

    return numero


# Recibe las 5 jugadas, sortea un número al azar en [0, 100] e informa si hay ganadores.
def loteria(j1, j2, j3, j4, j5):
    sorteado = random.randint(0, NUMERO_MAXIMO)
    print(f"El número sorteado es: {sorteado}")

    cantidad_ganadores = 0

    if j1 == sorteado:
        print("El jugador 1 ganó.")
        cantidad_ganadores += 1
    if j2 == sorteado:
        print("El jugador 2 ganó.")
        cantidad_ganadores += 1
    if j3 == sorteado:
        print("El jugador 3 ganó.")
        cantidad_ganadores += 1
    if j4 == sorteado:
        print("El jugador 4 ganó.")
        cantidad_ganadores += 1
    if j5 == sorteado:
        print("El jugador 5 ganó.")
        cantidad_ganadores += 1

    if cantidad_ganadores == 0:
        print("No hubo ganadores.")
    elif cantidad_ganadores == 1:
        print("Hubo 1 ganador.")
    else:
        print(f"Hubo {cantidad_ganadores} ganadores.")

    return sorteado, cantidad_ganadores


# --- Algoritmo principal ---
print("Lotería de 5 jugadores")

j1 = jugada(1)
j2 = jugada(2)
j3 = jugada(3)
j4 = jugada(4)
j5 = jugada(5)

loteria(j1, j2, j3, j4, j5)
