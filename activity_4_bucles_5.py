# 📌 Consigna: 
# Diseñar un algoritmo que solicite al usuario se ingresen dos números enteros positivos, 
# y muestre en pantalla la división del primero por la serie que conforma el segundo. 
# Ejemplo: num1 = 10, num2 = 3, la salida deberá mostrar el resultado de dividir 10/1, 10/2 y 10/3. 
# El programa deberá validar que los dos números ingresados sean positivos, en caso contrario 
# mostrar un mensaje tal como “Número ingresado no válido” y volver a solicitarlo hasta cumplir 
# con la condición de validación.

num1 = int(input("Ingrese un número entero positivo: "))
num2 = int(input("Ingrese un número entero positivo: "))

while num1 <= 0 or num2 <= 0:
    print("Número ingresado no válido")
    num1 = int(input("Ingrese un número entero positivo: "))
    num2 = int(input("Ingrese un número entero positivo: "))

for i in range(1, num2 + 1):
    print(f"{num1} / {i} = {num1 / i}")

# 💡 Solución alternativa: validar cada número por separado
# (así no se vuelve a pedir un número que ya era válido)

num1 = int(input("Ingrese un número entero positivo: "))
while num1 <= 0:
    print("Número ingresado no válido")
    num1 = int(input("Ingrese un número entero positivo: "))

num2 = int(input("Ingrese un número entero positivo: "))
while num2 <= 0:
    print("Número ingresado no válido")
    num2 = int(input("Ingrese un número entero positivo: "))

for i in range(1, num2 + 1):
    print(f"{num1} / {i} = {num1 / i}")