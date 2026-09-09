# 📌 Consigna:
#
# Crear una función que reciba 4 argumentos: x1, y1, x2, y2 y devuelva la distancia entre dos puntos en el plano.
#
# 1. Importar math.
# 2. Crear una función distancia(x1, y1, x2, y2) que reciba como argumentos los puntos del plano y devuelva la distancia calculada. Utilizar la fórmula de distancia:
#   distancia = raiz cuadrada de [(x2-x1)**2 + (y2-y1)**2]
# 3. Usar la función math.sqrt() para calcular la raíz cuadrada.
# 4. Llamar a la función con los valores (1, 2) y (4, 6).
# 5. Mostrar el resultado por consola.

import math


# Distancia euclidiana entre dos puntos del plano: (x1, y1) y (x2, y2).
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Puntos pedidos en la consigna: (1, 2) y (4, 6)
x1 = 1
y1 = 2
x2 = 4
y2 = 6

resultado = distancia(x1, y1, x2, y2)
print(f"La distancia entre ({x1}, {y1}) y ({x2}, {y2}) es: {resultado}")
