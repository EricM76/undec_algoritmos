# 📌 Consigna:
# Escribe un programa que permita actualizar el precio de un producto en un diccionario de productos y precios. Si el producto no existe, se debe añadir. 
# El diccionario inicial de productos es el siguiente:
# productos = {
#     "pan": 2100.5,
#     "leche": 1350.6,
#     "huevos": 323.0
# }

# Crear el diccionario inicial de productos.
productos = {
    "pan": 2100.5,
    "leche": 1350.6,
    "huevos": 323.0
}

# Solicitar el nombre del producto y el nuevo precio.
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))

# Actualizar el precio si el producto existe, o añadirlo si no existe.
if producto in productos:
    productos[producto] = precio
    print(f"Se actualizó el precio de {producto}.")
else:
    productos[producto] = precio
    print(f"Se añadió el producto {producto}.")

# Mostrar el diccionario actualizado.
print(productos)
