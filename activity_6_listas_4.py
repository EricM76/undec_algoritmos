# 📌 Consigna:
# Tenemos una lista con las edades de un grupo de personas. Vamos a determinar la edad menor y mayor del grupo.
#
# Pasos:
#
# 1. Obtener la cantidad de edades.
# 2. Obtener la edad menor del grupo.
# 3. Obtener la edad mayor del grupo.
# 4. Ordenar de menor a mayor las edades.
# 5. Mostrar todos los resultados por consola.

edades = [25, 18, 42, 31, 19, 36, 22]

# 1. Obtener la cantidad de edades.
cantidad_edades = len(edades)

# 2. Obtener la edad menor del grupo.
edad_menor = min(edades)

# 3. Obtener la edad mayor del grupo.
edad_mayor = max(edades)

# 4. Ordenar de menor a mayor las edades.
edades.sort()

# 5. Mostrar todos los resultados por consola.
print(f"Cantidad de edades: {cantidad_edades}")
print(f"Edad menor: {edad_menor}")
print(f"Edad mayor: {edad_mayor}")
print(f"Edades ordenadas: {edades}")
