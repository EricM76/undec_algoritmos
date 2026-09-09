# 📌 Consigna:
# 
# Un estudiante tiene una lista con sus notas. Queremos calcular el promedio total.
# 
# Pasos:
# 1. Obtener la suma de las notas de la lista.
# 2. Obtener la cantidad de notas.
# 3. Calcular el promedio.
# 4. Mostrar todos los resultados por consola.

notas = [7, 8, 9, 10, 10]

# 1. Obtener la suma de las notas de la lista.
suma_notas = sum(notas)

# 2. Obtener la cantidad de notas.
cantidad_notas = len(notas)

# 3. Calcular el promedio.
promedio = suma_notas / cantidad_notas

# 4. Mostrar todos los resultados por consola.
print(f"Suma de las notas: {suma_notas}")
print(f"Cantidad de notas: {cantidad_notas}")
print(f"Promedio: {promedio}")