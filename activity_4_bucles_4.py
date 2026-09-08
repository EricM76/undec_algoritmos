# 📌 Consigna:
# Crear un minijuego para lanzar un dado hasta 10 veces.
# - El objetivo es ganar si la suma total de los dados supera los 38 puntos.
# - Si no se logra en 10 tiradas, se pierde.
# 
# 🔧 Pasos a seguir:
# 
# 1. Importar randint del módulo random.
# 2. Crear tres variables iniciales:
# - dado = 0
# - contador = 0
# - puntaje = 0
# 3. Crear un bucle while que se ejecute mientras:
# - contador < 10 y
# - puntaje < 38
# 4. Dentro del bucle while:
# - Generar un número aleatorio entre 1 y 6 con randint().
# - Sumar ese número a puntaje.
# - Incrementar el contador en 1.
# - Mostrar el número obtenido.
# 5. Al salir del bucle, mostrar el puntaje total.
# 6. Si puntaje >= 38, mostrar "Ganaste", si no, mostrar "Perdiste".

# 💡 Ejemplo de salida esperada:
# Tirada 1: 4
# Tirada 2: 6
# ...
# El puntaje total es: 41
# Ganaste

from random import randint

dado = 0
contador = 0
puntaje = 0

while contador < 10 and puntaje < 38:
    dado = randint(1, 6)
    puntaje += dado
    contador += 1
    print(f"Tirada {contador}: {dado}")

print(f"El puntaje total es: {puntaje}")

if puntaje >= 38:
    print("Ganaste")
else:
    print("Perdiste")
