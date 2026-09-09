# 📌 Consigna:
# Escribe un programa que elimine las claves de un diccionario que tienen valores negativos. Usa un diccionario con números enteros como el siguiente:
# numeros = {
#     "a": 5,
#     "b": -3,
#     "c": 8,
#     "d": -1
# }

# Crear el diccionario inicial.
numeros = {
    "a": 5,
    "b": -3,
    "c": 8,
    "d": -1
}

# Eliminar las claves que tienen valores negativos.
# Se recorre una copia de las claves para poder borrar del diccionario original.
for clave in list(numeros.keys()):
    if numeros[clave] < 0:
        del numeros[clave]

# Mostrar el diccionario resultante.
print(numeros)
