# 📌 Consigna:
# Los pacientes con síntomas de una cierta enfermedad son ingresados en el hospital si tienen un
# valor superior a 0.6 en la medición de un determinado índice, y son operados si el valor es superior a 0.9.
# Escribir un programa que lea desde teclado el número de pacientes N a cargar, seguido de la edad y el índice de cada paciente,
# y calcule la edad media de los pacientes analizados así como la edad media de los ingresados y la
# edad media de los operados.

# Umbrales del índice según la consigna.
# Se usan constantes para no repetir 0.6 y 0.9 sueltos en el código.
INDICE_INGRESO = 0.6      # si el índice es mayor a esto, el paciente se ingresa
INDICE_OPERACION = 0.9    # si el índice es mayor a esto, el paciente se opera

print("===== CARGA MANUAL =====")

# Pedimos cuántos pacientes se van a cargar (N de la consigna)
cantidad_pacientes = int(input("Ingrese la cantidad de pacientes a cargar: "))
# Un 0 o un negativo no tiene sentido: se pide de nuevo hasta que sea > 0
while cantidad_pacientes <= 0:
    print("Cantidad ingresada no válida")
    cantidad_pacientes = int(input("Ingrese la cantidad de pacientes a cargar: "))

# Para un promedio hace falta: suma de valores / cantidad de valores
# Acumuladores de TODOS los pacientes analizados (todos los que se cargan)
suma_edades = 0

# Acumuladores de los INGRESADOS (índice > 0.6)
# Hace falta un contador aparte porque no todos los pacientes se ingresan
suma_edades_ingresados = 0
cant_ingresados = 0

# Acumuladores de los OPERADOS (índice > 0.9)
# También va un contador aparte: puede no haber ningún operado
suma_edades_operados = 0
cant_operados = 0

# Recorremos cada paciente. El +1 hace que range llegue hasta cantidad_pacientes inclusive
for paciente in range(1, cantidad_pacientes + 1):
    print(f"\n--- Paciente {paciente} ---")

    # Pedimos la edad y validamos que no sea negativa
    edad = int(input("Ingrese la edad: "))
    while edad < 0:
        print("Edad ingresada no válida")
        edad = int(input("Ingrese la edad: "))

    # El índice es un decimal (float), no un entero.
    # Un índice negativo no tiene sentido; se pide de nuevo hasta que sea >= 0
    indice = float(input("Ingrese el índice: "))
    while indice < 0:
        print("Índice ingresado no válido")
        indice = float(input("Ingrese el índice: "))

    # Todos los pacientes cargados se consideran "analizados"
    suma_edades += edad

    # Clasificamos según el índice.
    # Un operado (índice > 0.9) también es ingresado, porque 0.9 ya es mayor a 0.6.
    # Por eso los dos if van separados y no son excluyentes.
    if indice > INDICE_INGRESO:
        suma_edades_ingresados += edad
        cant_ingresados += 1

    if indice > INDICE_OPERACION:
        suma_edades_operados += edad
        cant_operados += 1

# Mostramos los resultados de la carga manual
print("\n===== RESULTADOS (CARGA MANUAL) =====")
# Acá sí se puede dividir directo: ya validamos que cantidad_pacientes > 0
print(f"Edad media de los pacientes analizados: {suma_edades / cantidad_pacientes}")

# Si nadie superó 0.6, cant_ingresados queda en 0 y no se puede dividir
if cant_ingresados > 0:
    print(f"Edad media de los ingresados: {suma_edades_ingresados / cant_ingresados}")
else:
    print("No hay pacientes ingresados")

# Misma precaución para los operados: puede no haber ninguno con índice > 0.9
if cant_operados > 0:
    print(f"Edad media de los operados: {suma_edades_operados / cant_operados}")
else:
    print("No hay pacientes operados")

# 💡 Solución alternativa: misma lógica, pero edad e índice se generan al azar (sin teclado)

from random import randint, random  # randint = enteros; random = decimales entre 0 y 1

CANTIDAD_PACIENTES = 8  # en esta versión la cantidad está fija

print("\n===== CARGA ALEATORIA =====")
print(f"Cantidad de pacientes: {CANTIDAD_PACIENTES}")

# Reiniciamos los acumuladores para no mezclar los datos con la carga manual
suma_edades = 0
suma_edades_ingresados = 0
cant_ingresados = 0
suma_edades_operados = 0
cant_operados = 0

for paciente in range(1, CANTIDAD_PACIENTES + 1):
    # randint incluye ambos extremos: puede salir 1 o 90
    edad = randint(1, 90)
    # random() da un decimal entre 0.0 y 1.0; round(..., 2) lo deja con 2 decimales (ej: 0.73)
    indice = round(random(), 2)
    print(f"Paciente {paciente}: edad {edad}, índice {indice}")

    # A partir de acá la lógica es idéntica a la carga manual
    suma_edades += edad

    if indice > INDICE_INGRESO:
        suma_edades_ingresados += edad
        cant_ingresados += 1

    if indice > INDICE_OPERACION:
        suma_edades_operados += edad
        cant_operados += 1

print("\n===== RESULTADOS (CARGA ALEATORIA) =====")
print(f"Edad media de los pacientes analizados: {suma_edades / CANTIDAD_PACIENTES}")

if cant_ingresados > 0:
    print(f"Edad media de los ingresados: {suma_edades_ingresados / cant_ingresados}")
else:
    print("No hay pacientes ingresados")

if cant_operados > 0:
    print(f"Edad media de los operados: {suma_edades_operados / cant_operados}")
else:
    print("No hay pacientes operados")
