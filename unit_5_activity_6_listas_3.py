# 📌 Consigna:
# Una lista de frutas tiene elementos mal cargados. Hay que corregirlos y luego verificar información.
# frutas = ["banana", "patata", "tomate", "uva", "cebolla", "pera"]
#
# Pasos:
# 1. Cambiar:
#    "patata" por "fresa"
#    "tomate" por "manzana"
#    "cebolla" por "durazno"
# 2. Ordenar alfabéticamente.
# 3. Mostrar la lista modificada.
# 4. Verificar si "maracuyá" está en la lista.
# 5. Invertir el orden y mostrarla.

frutas = ["banana", "patata", "tomate", "uva", "cebolla", "pera"]
print(f"Lista original: {frutas}")

# 1. Cambiar los elementos mal cargados.
frutas[frutas.index("patata")] = "fresa"
frutas[frutas.index("tomate")] = "manzana"
frutas[frutas.index("cebolla")] = "durazno"

# 2. Ordenar alfabéticamente.
frutas.sort()

# 3. Mostrar la lista modificada.
print(f"Lista modificada: {frutas}")

# 4. Verificar si "maracuyá" está en la lista.
if "maracuyá" in frutas:
    print("maracuyá está en la lista.")
else:
    print("maracuyá no está en la lista.")

# 5. Invertir el orden y mostrarla.
frutas.reverse()
print(f"Lista invertida: {frutas}")
