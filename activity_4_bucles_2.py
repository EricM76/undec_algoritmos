# 📌 Consigna:
# Pedirle al usuario que ingrese un número positivo (usar input() e int() para convertirlo).
# - Mostrar una cuenta regresiva desde ese número hasta 0, de uno en uno.
# - Al finalizar, mostrar el mensaje "¡Despegue!".

numero = int(input("Ingrese un número positivo: "))

for i in range(numero, -1, -1):
    print(i)

print("¡Despegue!")