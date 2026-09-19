# 📌 Consigna:
# Se dispone de los datos sobre las edades y coeficientes de inteligencia (CI) de los hijos de 
# varias familias, dicho CI puede variar entre los valores 24 y 130. Se solicita diseñar un programa 
# que permita leer el número de familias y el número de hijos de cada familia así como también la 
# edad y el CI de cada hijo, y calcule:
# - El número máximo, mínimo y promedio de hijos por familia.
# - El CI máximo, mínimo y promedio de todos los hijos.
# - El CI promedio de los hijos menores de 6 años.
# - El CI promedio de los hijos mayores de 6 años

# Límites del CI según la consigna
CI_MIN = 24
CI_MAX = 130

print("===== CARGA MANUAL =====")

# Pedimos la cantidad de familias y validamos que sea mayor a 0
cantidad_familias = int(input("Ingrese la cantidad de familias: "))
while cantidad_familias <= 0:
    print("Cantidad ingresada no válida")
    cantidad_familias = int(input("Ingrese la cantidad de familias: "))

# Acumuladores para el máximo, mínimo y promedio de hijos por familia
max_hijos = 0
min_hijos = 0
suma_hijos = 0
primera_familia = True  # bandera: el primer valor se usa como referencia de max/min

# Acumuladores para el máximo, mínimo y promedio de CI de todos los hijos
max_ci = 0
min_ci = 0
suma_ci = 0
total_hijos = 0
primer_hijo = True  # bandera: el primer CI se usa como referencia de max/min

# Acumuladores para los promedios de CI según la edad
# (los de exactamente 6 años no entran en menores ni en mayores)
suma_ci_menores = 0
cant_menores = 0
suma_ci_mayores = 0
cant_mayores = 0

# Recorremos cada familia
for familia in range(1, cantidad_familias + 1):
    print(f"\n--- Familia {familia} ---")

    # Pedimos la cantidad de hijos de esta familia y validamos que sea mayor a 0
    hijos = int(input("Ingrese la cantidad de hijos: "))
    while hijos <= 0:
        print("Cantidad ingresada no válida")
        hijos = int(input("Ingrese la cantidad de hijos: "))

    suma_hijos += hijos  # sirve después para calcular el promedio

    # Actualizamos máximo y mínimo de hijos
    if primera_familia:
        # En la primera familia, ese valor es a la vez máximo y mínimo
        max_hijos = hijos
        min_hijos = hijos
        primera_familia = False
    else:
        if hijos > max_hijos:
            max_hijos = hijos
        if hijos < min_hijos:
            min_hijos = hijos

    # Recorremos cada hijo de la familia actual
    for hijo in range(1, hijos + 1):
        print(f"\nHijo {hijo}:")

        # Validamos que la edad no sea negativa
        edad = int(input("Ingrese la edad: "))
        while edad < 0:
            print("Edad ingresada no válida")
            edad = int(input("Ingrese la edad: "))

        # Validamos que el CI esté entre 24 y 130
        ci = int(input(f"Ingrese el CI ({CI_MIN} a {CI_MAX}): "))
        while ci < CI_MIN or ci > CI_MAX:
            print("CI ingresado no válido")
            ci = int(input(f"Ingrese el CI ({CI_MIN} a {CI_MAX}): "))

        total_hijos += 1  # contamos todos los hijos (de todas las familias)
        suma_ci += ci     # acumulamos para el promedio general

        # Actualizamos máximo y mínimo de CI
        if primer_hijo:
            max_ci = ci
            min_ci = ci
            primer_hijo = False
        else:
            if ci > max_ci:
                max_ci = ci
            if ci < min_ci:
                min_ci = ci

        # Clasificamos el CI según la edad (menor de 6 o mayor de 6)
        if edad < 6:
            suma_ci_menores += ci
            cant_menores += 1
        elif edad > 6:
            suma_ci_mayores += ci
            cant_mayores += 1

# Mostramos los resultados de la carga manual
print("\n===== RESULTADOS (CARGA MANUAL) =====")
print(f"Máximo de hijos por familia: {max_hijos}")
print(f"Mínimo de hijos por familia: {min_hijos}")
print(f"Promedio de hijos por familia: {suma_hijos / cantidad_familias}")

print(f"CI máximo: {max_ci}")
print(f"CI mínimo: {min_ci}")
print(f"CI promedio de todos los hijos: {suma_ci / total_hijos}")

# Evitamos dividir por 0 si no hubo hijos en ese grupo de edad
if cant_menores > 0:
    print(f"CI promedio de hijos menores de 6 años: {suma_ci_menores / cant_menores}")
else:
    print("No hay hijos menores de 6 años")

if cant_mayores > 0:
    print(f"CI promedio de hijos mayores de 6 años: {suma_ci_mayores / cant_mayores}")
else:
    print("No hay hijos mayores de 6 años")

# 💡 Solución alternativa: carga aleatoria de un máximo de 5 familias,
# con 2 o 3 hijos, edades entre 6 y 12, y CI entre 24 y 130
# La lógica es la misma; solo cambia cómo se generan los datos.

from random import randint  # randint(a, b) genera un entero al azar entre a y b inclusive

MAX_FAMILIAS = 5  # tope pedido para la carga aleatoria

print("\n===== CARGA ALEATORIA =====")

# Se elige al azar cuántas familias hay (entre 1 y 5)
cantidad_familias = randint(1, MAX_FAMILIAS)
print(f"Cantidad de familias: {cantidad_familias}")

# Reiniciamos los acumuladores para no mezclarlos con la carga manual
max_hijos = 0
min_hijos = 0
suma_hijos = 0
primera_familia = True

max_ci = 0
min_ci = 0
suma_ci = 0
total_hijos = 0
primer_hijo = True

suma_ci_menores = 0
cant_menores = 0
suma_ci_mayores = 0
cant_mayores = 0

for familia in range(1, cantidad_familias + 1):
    print(f"\n--- Familia {familia} ---")

    hijos = randint(2, 3)  # cada familia tiene 2 o 3 hijos
    print(f"Cantidad de hijos: {hijos}")

    suma_hijos += hijos

    if primera_familia:
        max_hijos = hijos
        min_hijos = hijos
        primera_familia = False
    else:
        if hijos > max_hijos:
            max_hijos = hijos
        if hijos < min_hijos:
            min_hijos = hijos

    for hijo in range(1, hijos + 1):
        edad = randint(6, 12)          # edades entre 6 y 12 (no habrá menores de 6)
        ci = randint(CI_MIN, CI_MAX)   # CI dentro del rango de la consigna
        print(f"Hijo {hijo}: edad {edad}, CI {ci}")

        total_hijos += 1
        suma_ci += ci

        if primer_hijo:
            max_ci = ci
            min_ci = ci
            primer_hijo = False
        else:
            if ci > max_ci:
                max_ci = ci
            if ci < min_ci:
                min_ci = ci

        # Con edades 6-12: los de 6 no entran en ningún grupo; los de 7 a 12 sí en mayores
        if edad < 6:
            suma_ci_menores += ci
            cant_menores += 1
        elif edad > 6:
            suma_ci_mayores += ci
            cant_mayores += 1

print("\n===== RESULTADOS (CARGA ALEATORIA) =====")
print(f"Máximo de hijos por familia: {max_hijos}")
print(f"Mínimo de hijos por familia: {min_hijos}")
print(f"Promedio de hijos por familia: {suma_hijos / cantidad_familias}")

print(f"CI máximo: {max_ci}")
print(f"CI mínimo: {min_ci}")
print(f"CI promedio de todos los hijos: {suma_ci / total_hijos}")

if cant_menores > 0:
    print(f"CI promedio de hijos menores de 6 años: {suma_ci_menores / cant_menores}")
else:
    print("No hay hijos menores de 6 años")

if cant_mayores > 0:
    print(f"CI promedio de hijos mayores de 6 años: {suma_ci_mayores / cant_mayores}")
else:
    print("No hay hijos mayores de 6 años")
