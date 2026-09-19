# 📌 Consigna:
# Crear un algoritmo que compare cuatro números ingresados por el usuario y muestre cuál es mayor.
# - Pedir al usuario que ingrese cuatro números (convertidos a int).
# - Usar condicionales if, elif y else para:
# - Mostrar si el primer número es mayor.
# - Mostrar si el segundo número es mayor.
# - Mostrar si el tercer número es mayor.
# - Mostrar si el cuarto número es mayor.
# - O si todos son iguales.

# Lista con los 4 números: [0] primero, [1] segundo, [2] tercero, [3] cuarto
input_numeros = [
    int(input("Ingrese el primer número: ")),
    int(input("Ingrese el segundo número: ")),
    int(input("Ingrese el tercer número: ")),
    int(input("Ingrese el cuarto número: "))]

# Un número es "el mayor" solo si es ESTRICTAMENTE más grande que los otros tres
# (por eso se usa ">" y no ">=": si hay empate, no entra en ningún if)
if input_numeros[0] > input_numeros[1] and input_numeros[0] > input_numeros[2] and input_numeros[0] > input_numeros[3]:
    print(f"El primer número es mayor: {input_numeros[0]}")
elif input_numeros[1] > input_numeros[0] and input_numeros[1] > input_numeros[2] and input_numeros[1] > input_numeros[3]:
    print(f"El segundo número es mayor: {input_numeros[1]}")
elif input_numeros[2] > input_numeros[0] and input_numeros[2] > input_numeros[1] and input_numeros[2] > input_numeros[3]:
    print(f"El tercer número es mayor: {input_numeros[2]}")
elif input_numeros[3] > input_numeros[0] and input_numeros[3] > input_numeros[1] and input_numeros[3] > input_numeros[2]:
    print(f"El cuarto número es mayor: {input_numeros[3]}")
else:
    # Nadie ganó por diferencia: o son los cuatro iguales, o hay un empate en el tope
    print("Todos los números son iguales")
