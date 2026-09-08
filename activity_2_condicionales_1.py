# 📌 Consigna:
# Generar un algoritmo para indicar si el usuario tiene la edad necesaria para conducir.
# - Crear una variable para guardar la edad del usuario con input() y convertirla a número con int().
# - Crear una estructura condicional if que evalúe si la edad es mayor o igual a 16.
# - Si se cumple, mostrar: "Tienes permitido conducir".
# - Si no se cumple, mostrar: "No tienes permitido conducir".

# input() siempre trae texto; int() lo convierte a número para poder comparar
input_edad = int(input("Ingrese su edad: "))

# >= 16 incluye justo los 16 años (si usáramos > 16, a los 16 no podría)
if input_edad >= 16:
    print("Tienes permitido conducir")
else:
    # Cualquier edad menor a 16 cae acá
    print("No tienes permitido conducir")
