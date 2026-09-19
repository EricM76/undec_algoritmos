# 📌 Consigna:
# Escribe un programa que cuente cuántas veces aparece cada letra en una palabra dada por el usuario, usando un diccionario con estructura letra:frecuencia.

# Crear un diccionario para contar las letras.
letras = {}

# Solicitar la palabra al usuario.
palabra = input("Ingrese una palabra: ")

# Contar las letras de la palabra.
for letra in palabra:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

# Mostrar el diccionario con la frecuencia de cada letra.
print(letras)
