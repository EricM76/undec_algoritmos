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

MESES = 6
LIMITE = 30000

cantidad_vendedores = int(input("Ingrese la cantidad de vendedores contratados: "))
while cantidad_vendedores <= 0:
    print("Cantidad ingresada no válida")
    cantidad_vendedores = int(input("Ingrese la cantidad de vendedores contratados: "))

resumen = ""

for vendedor in range(1, cantidad_vendedores + 1):
    print(f"\n--- Carga de datos del vendedor {vendedor} ---")

    total_vendido = 0
    ventas_superaron = 0
    ventas_no_superaron = 0
    meses_sin_ventas = 0

    for mes in range(1, MESES + 1):
        monto = float(input(f"Ingrese el monto de ventas del mes {mes}: "))
        while monto < 0:
            print("Monto ingresado no válido")
            monto = float(input(f"Ingrese el monto de ventas del mes {mes}: "))

        total_vendido += monto

        if monto > LIMITE:
            ventas_superaron += 1
        else:
            ventas_no_superaron += 1

        if monto == 0:
            meses_sin_ventas += 1

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

