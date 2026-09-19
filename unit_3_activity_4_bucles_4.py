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

from random import randint  # para simular el dado (número al azar entre 1 y 6)

# Variables iniciales pedidas en la consigna
dado = 0       # último valor que salió (se pisa en cada tirada)
contador = 0   # cuántas tiradas llevamos (máximo 10)
puntaje = 0    # suma acumulada de todas las caras

# El while sigue mientras NO hayamos tirado 10 veces Y aún no llegamos a 38
# Con "and": alcanza con que falle UNA condición para salir
# - contador == 10 → se acabaron las tiradas
# - puntaje >= 38  → ya ganamos, no hace falta seguir tirando
while contador < 10 and puntaje < 38:
    dado = randint(1, 6)   # cara del dado (1 a 6 inclusive)
    puntaje += dado        # sumamos esa cara al total
    contador += 1          # una tirada más
    print(f"Tirada {contador}: {dado}")

print(f"El puntaje total es: {puntaje}")

# Si al salir del while el total llegó a 38 o más, ganamos; si no, perdimos
if puntaje >= 38:
    print("Ganaste")
else:
    print("Perdiste")
