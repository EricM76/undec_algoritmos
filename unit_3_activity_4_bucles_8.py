# 📌 Consigna: 
# Una fábrica de productos alimenticios local ha decidido contratar vendedores para intentar ofrecer 
# sus productos y ganar mercado fuera de la provincia. Se solicita diseñar un programa que permita 
# cargar por teclado los montos de ventas realizadas por los vendedores durante los últimos 6 meses 
# (en caso de no haber realizado ventas en algún mes deberá cargarse 0). Además se deberá determinar 
# para cada vendedor:
# - El monto total vendido. 
# - Cuantas ventas superaron los $30000
# - Cuantas ventas no superaron los $30000
# - Si todos los meses registraron ventas.
# - Si hubo meses sin ventas y cuantos.
# La cantidad de vendedores contratados se solicita al iniciar el programa.

# Constantes: 6 meses a analizar y el umbral de $30000 pedido en la consigna
MESES = 6
LIMITE = 30000

# Pedimos cuántos vendedores hay y validamos que sea un número positivo
cantidad_vendedores = int(input("Ingrese la cantidad de vendedores contratados: "))
while cantidad_vendedores <= 0:
    print("Cantidad ingresada no válida")
    cantidad_vendedores = int(input("Ingrese la cantidad de vendedores contratados: "))

# Acumulamos el texto del informe de todos los vendedores para mostrarlo al final
resumen = ""

# Recorremos cada vendedor (el +1 hace que range llegue hasta cantidad_vendedores inclusive)
for vendedor in range(1, cantidad_vendedores + 1):
    print(f"\n--- Carga de datos del vendedor {vendedor} ---")

    # Contadores de ESTE vendedor: se reinician en cada vuelta del for
    total_vendido = 0          # suma de los 6 montos
    ventas_superaron = 0       # meses con monto > 30000
    ventas_no_superaron = 0    # meses con monto <= 30000 (incluye 0)
    meses_sin_ventas = 0       # meses con monto exactamente 0

    # Pedimos el monto de cada uno de los 6 meses
    for mes in range(1, MESES + 1):
        monto = float(input(f"Ingrese el monto de ventas del mes {mes}: "))
        # Un monto negativo no tiene sentido; se pide de nuevo hasta que sea >= 0
        while monto < 0:
            print("Monto ingresado no válido")
            monto = float(input(f"Ingrese el monto de ventas del mes {mes}: "))

        total_vendido += monto  # vamos sumando mes a mes

        # Clasificamos el mes según el límite de $30000
        if monto > LIMITE:
            ventas_superaron += 1
        else:
            ventas_no_superaron += 1

        # Si el mes quedó en 0, no hubo ventas
        if monto == 0:
            meses_sin_ventas += 1

    # Armamos el bloque de texto de este vendedor y lo pegamos al resumen general
    resumen += f"\n--- Vendedor {vendedor} ---\n"
    resumen += f"Monto total vendido: ${total_vendido}\n"
    resumen += f"Tuvo {ventas_superaron} ventas que superaron los ${LIMITE}\n"
    resumen += f"Tuvo {ventas_no_superaron} ventas que no superaron los ${LIMITE}\n"

    # Si meses_sin_ventas quedó en 0, todos los meses tuvieron ventas
    if meses_sin_ventas == 0:
        resumen += "Todos los meses registraron ventas\n"
    else:
        resumen += f"Hubo {meses_sin_ventas} mes(es) sin ventas\n"

print("\n===== RESUMEN POR VENDEDOR =====")
print(resumen)

# 💡 Solución alternativa: misma lógica, pero los montos se generan al azar (sin teclado)

from random import randint

CANTIDAD_VENDEDORES = 3  # en esta versión la cantidad está fija
resumen = ""             # reiniciamos el texto para el segundo informe

print("\n===== CARGA ALEATORIA DE 3 VENDEDORES =====")

for vendedor in range(1, CANTIDAD_VENDEDORES + 1):
    print(f"\n--- Carga de datos del vendedor {vendedor} ---")

    # Mismos contadores que en la carga manual
    total_vendido = 0
    ventas_superaron = 0
    ventas_no_superaron = 0
    meses_sin_ventas = 0

    for mes in range(1, MESES + 1):
        # randint incluye ambos extremos: puede salir 0 (sin ventas) o hasta 50000
        monto = randint(0, 50000)
        print(f"Mes {mes}: ${monto}")

        total_vendido += monto

        if monto > LIMITE:
            ventas_superaron += 1
        else:
            ventas_no_superaron += 1

        if monto == 0:
            meses_sin_ventas += 1

    # El armado del informe es idéntico a la versión con teclado
    resumen += f"\n--- Vendedor {vendedor} ---\n"
    resumen += f"Monto total vendido: ${total_vendido}\n"
    resumen += f"Tuvo {ventas_superaron} ventas que superaron los ${LIMITE}\n"
    resumen += f"Tuvo {ventas_no_superaron} ventas que no superaron los ${LIMITE}\n"

    if meses_sin_ventas == 0:
        resumen += "Todos los meses registraron ventas\n"
    else:
        resumen += f"Hubo {meses_sin_ventas} mes(es) sin ventas\n"

print("\n===== RESUMEN POR VENDEDOR =====")
print(resumen)

