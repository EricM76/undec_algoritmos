# 📌 Consigna:
# Escribe un programa que tome dos listas, una de claves y otra de valores, y cree un diccionario uniendo ambas listas. 
# Las listas originales son las siguientes:
# - claves = ["nombre", "edad", "ciudad"]
# - valores = ["Ana", 28, "Barcelona"]

# Crear las listas originales.
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Barcelona"]

# Crear el diccionario uniendo ambas listas.
persona = {}
for i in range(len(claves)):
    persona[claves[i]] = valores[i]

# Mostrar el diccionario resultante.
print(persona)
