# Una concesionaria de vehículos nos pidió hacer un inventario con los datos básicos de sus autos.
# 📌 Pasos:
#
# Crear una variable llamada auto1 que contenga un diccionario con al menos estas claves:
# "color"
# "cantidad_puertas"
# "marca"
# Repetir el punto anterior para crear auto2, auto3 y auto4.
# Modificar el color del auto2 utilizando la notación de corchetes.
# Mostrar por consola el nuevo color de auto2.

# Crear auto1, auto2, auto3 y auto4.
auto1 = {
    "color": "rojo",
    "cantidad_puertas": 4,
    "marca": "Ford"
}

auto2 = {
    "color": "azul",
    "cantidad_puertas": 2,
    "marca": "Chevrolet"
}

auto3 = {
    "color": "blanco",
    "cantidad_puertas": 5,
    "marca": "Toyota"
}

auto4 = {
    "color": "negro",
    "cantidad_puertas": 4,
    "marca": "Volkswagen"
}

# Modificar el color del auto2 utilizando la notación de corchetes.
auto2["color"] = "gris"

# Mostrar por consola el nuevo color de auto2.
print(f"El nuevo color de auto2 es: {auto2['color']}")
