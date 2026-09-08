# 📌 Consigna:
# Pedirle al usuario que ingrese un número positivo (usar input() e int() para convertirlo).
# - Mostrar una cuenta regresiva desde ese número hasta 0, de uno en uno.
# - Al finalizar, mostrar el mensaje "¡Despegue!".

# Pedimos el número de partida y lo convertimos a entero
numero = int(input("Ingrese un número positivo: "))

# range(inicio, fin, paso):
# - empieza en "numero"
# - el -1 del medio es el tope EXCLUSIVO, así que sí incluye el 0
# - el último -1 hace que baje de a 1 (cuenta regresiva)
# Ej: numero=3 → 3, 2, 1, 0
for i in range(numero, -1, -1):
    print(i)

# Recién cuando el for termina (llegamos a 0) se muestra el mensaje
print("¡Despegue!")