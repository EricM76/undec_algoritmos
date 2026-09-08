# 📌 Consigna:
# Generar un algoritmo para consultar si hay o no un gusto de helado disponible.
# - Crear una variable que guarde el gusto ingresado por el usuario con input().
# - Evaluar con if si el gusto ingresado coincide con alguno de estos: "chocolate", "vainilla", "frutilla" o "dulce de leche".
# - Si está disponible, mostrar: "Sí, hay ____".
# - Si no, mostrar: "No hay ____".

# Pedimos el gusto tal cual lo escribe el usuario (sin normalizar)
input_gusto = input("Ingrese su gusto de helado: ")

# Con "or" alcanza con que coincida CON UNO de los 4 nombres
# La comparación es exacta: "Chocolate" o "CHOCOLATE" no entran (mayúsculas distintas)
if input_gusto == "chocolate" or input_gusto == "vainilla" or input_gusto == "frutilla" or input_gusto == "dulce de leche":
    print(f"Sí, hay {input_gusto}")
else:
    # No coincidió con ninguno de los disponibles
    print(f"No hay {input_gusto}")