# 📌 Consigna:
# Generar un programa para una fábrica de alimentos que posee una cámara de frío para el almacenamiento de vegetales triturados congelados, 
# la misma debe mantenerse siempre por debajo de 0 °C para asegurar una adecuada conservación. 
# Últimamente ha tenido muchas pérdidas de materia prima debido a que la inestabilidad de las líneas eléctricas  ocasiona que la cámara quedé 
# sin suministro eléctrico y en consecuencia aumente su temperatura. 
# Como solución se desea diseñar un programa que permita tomar la temperatura registrada en el sensor de la cámara de frío y emita 
# mensajes de alerta tal como “PELIGRO, TEMPERATURA EN AUMENTO” cuando la temperatura supere los 0°. En caso contrario no emitir ningún mensaje
# La temperatura se leerá por teclado, queda fuera del análisis y diseño la captura de datos desde un sensor de temperatura.

# Leemos la temperatura por teclado (la consigna no pide conectar un sensor real)
input_temperatura = int(input("Ingrese la temperatura registrada en el sensor de la cámara de frío: "))

# La cámara debe estar por debajo de 0 °C. Solo alertamos si SUPERÓ ese límite
# Si está en 0 o bajo cero, no se imprime nada (la consigna: no emitir mensaje)
if input_temperatura > 0:
    print("PELIGRO, TEMPERATURA EN AUMENTO")

# Simulación de 10 lecturas aleatorias del sensor de la cámara de frío.
# La temperatura oscila entre -10 °C y 10 °C.
# Si supera los 0 °C se emite la alerta; si no, no se muestra ese mensaje.

import random

# 10 vueltas: en cada una se "lee" el sensor con un número al azar
for i in range(10):
    temperatura = random.randint(-10, 10)  # incluye -10 y 10
    print(f"Lectura {i + 1}: {temperatura} °C")  # i+1 para mostrar 1..10 y no 0..9
    # Misma regla que arriba: alerta solo si pasó de 0
    if temperatura > 0:
        print("PELIGRO, TEMPERATURA EN AUMENTO")
