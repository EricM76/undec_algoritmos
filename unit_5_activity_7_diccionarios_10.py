# 📌 Consigna:
#
# Escribe un programa que sume todos los valores numéricos de un diccionario dado y encuentre la clave con el
# valor más alto. El diccionario con los valores numéricos es el siguiente:
# diccionario = {
#     "a": 5,
#     "b": 12,
#     "c": 3,
#     "d": 7
# }

# Crear el diccionario inicial.
diccionario = {
    "a": 5,
    "b": 12,
    "c": 3,
    "d": 7
}

# Sumar todos los valores numéricos.
suma = 0
for valor in diccionario.values():
    suma += valor

# Encontrar la clave con el valor más alto.
clave_maxima = None
valor_maximo = None
for clave, valor in diccionario.items():
    if valor_maximo is None or valor > valor_maximo:
        valor_maximo = valor
        clave_maxima = clave

# Mostrar los resultados.
print("Suma de los valores:", suma)
print("Clave con el valor más alto:", clave_maxima)
print("Valor más alto:", valor_maximo)
