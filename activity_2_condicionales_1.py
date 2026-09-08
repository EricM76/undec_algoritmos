# 📌 Consigna:
# Generar un algoritmo para indicar si el usuario tiene la edad necesaria para conducir.
# - Crear una variable para guardar la edad del usuario con input() y convertirla a número con int().
# - Crear una estructura condicional if que evalúe si la edad es mayor o igual a 16.
# - Si se cumple, mostrar: "Tienes permitido conducir".
# - Si no se cumple, mostrar: "No tienes permitido conducir".

input_edad = int(input("Ingrese su edad: "))
if input_edad >= 16:
    print("Tienes permitido conducir")
else:
    print("No tienes permitido conducir")
