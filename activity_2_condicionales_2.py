# 📌 Consigna:
# Generar un algoritmo para consultar si hay o no un gusto de helado disponible.
# - Crear una variable que guarde el gusto ingresado por el usuario con input().
# - Evaluar con if si el gusto ingresado coincide con alguno de estos: "chocolate", "vainilla", "frutilla" o "dulce de leche".
# - Si está disponible, mostrar: "Sí, hay ____".
# - Si no, mostrar: "No hay ____".

input_gusto = input("Ingrese su gusto de helado: ")
if input_gusto == "chocolate" or input_gusto == "vainilla" or input_gusto == "frutilla" or input_gusto == "dulce de leche":
    print(f"Sí, hay {input_gusto}")
else:
    print(f"No hay {input_gusto}")