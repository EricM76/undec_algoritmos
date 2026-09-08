# 📌 Consigna: 
# Diseñar un algoritmo que solicite al usuario se ingresen dos números enteros positivos, 
# y muestre en pantalla la división del primero por la serie que conforma el segundo. 
# Ejemplo: num1 = 10, num2 = 3, la salida deberá mostrar el resultado de dividir 10/1, 10/2 y 10/3. 
# El programa deberá validar que los dos números ingresados sean positivos, en caso contrario 
# mostrar un mensaje tal como “Número ingresado no válido” y volver a solicitarlo hasta cumplir 
# con la condición de validación.

# Pedimos los dos números. Deben ser enteros positivos (mayores que 0)
num1 = int(input("Ingrese un número entero positivo: "))
num2 = int(input("Ingrese un número entero positivo: "))

# Si CUALQUIERA de los dos es <= 0, se vuelven a pedir AMBOS
# Desventaja: si solo uno era inválido, el que ya estaba bien se pide de nuevo
while num1 <= 0 or num2 <= 0:
    print("Número ingresado no válido")
    num1 = int(input("Ingrese un número entero positivo: "))
    num2 = int(input("Ingrese un número entero positivo: "))

# Recorremos la serie 1, 2, 3, ..., num2 (el +1 hace que range llegue hasta num2)
# En cada vuelta mostramos num1 dividido por el término actual de la serie
# Ej: num1=10, num2=3 → 10/1, 10/2, 10/3
for i in range(1, num2 + 1):
    print(f"{num1} / {i} = {num1 / i}")

# 💡 Solución alternativa: validar cada número por separado
# (así no se vuelve a pedir un número que ya era válido)

# Validamos num1 hasta que sea positivo
num1 = int(input("Ingrese un número entero positivo: "))
while num1 <= 0:
    print("Número ingresado no válido")
    num1 = int(input("Ingrese un número entero positivo: "))

# Recién acá pedimos num2; si falla, num1 no se toca
num2 = int(input("Ingrese un número entero positivo: "))
while num2 <= 0:
    print("Número ingresado no válido")
    num2 = int(input("Ingrese un número entero positivo: "))

# Misma serie de divisiones que en la primera versión
for i in range(1, num2 + 1):
    print(f"{num1} / {i} = {num1 / i}")