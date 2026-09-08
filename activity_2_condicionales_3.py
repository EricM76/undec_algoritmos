# 📌 Consigna:
# Crear un algoritmo que compare cuatro números ingresados por el usuario y muestre cuál es mayor.
# - Pedir al usuario que ingrese cuatro números (convertidos a int).
# - Usar condicionales if, elif y else para:
# - Mostrar si el primer número es mayor.
# - Mostrar si el segundo número es mayor.
# - Mostrar si el tercer número es mayor.
# - Mostrar si el cuarto número es mayor.
# - O si todos son iguales.

input_numeros = [
    int(input("Ingrese el primer número: ")), 
    int(input("Ingrese el segundo número: ")), 
    int(input("Ingrese el tercer número: ")), 
    int(input("Ingrese el cuarto número: "))]
if input_numeros[0] > input_numeros[1] and input_numeros[0] > input_numeros[2] and input_numeros[0] > input_numeros[3]:
    print(f"El primer número es mayor: {input_numeros[0]}")
elif input_numeros[1] > input_numeros[0] and input_numeros[1] > input_numeros[2] and input_numeros[1] > input_numeros[3]:
    print(f"El segundo número es mayor: {input_numeros[1]}")
elif input_numeros[2] > input_numeros[0] and input_numeros[2] > input_numeros[1] and input_numeros[2] > input_numeros[3]:
    print(f"El tercer número es mayor: {input_numeros[2]}")
elif input_numeros[3] > input_numeros[0] and input_numeros[3] > input_numeros[1] and input_numeros[3] > input_numeros[2]:
    print(f"El cuarto número es mayor: {input_numeros[3]}")
else:
    print("Todos los números son iguales")
