# 📌 Consigna:
# 1.Importar el módulo random.
# 2.Crear 5 variables, donde cada una guarde un número aleatorio. (No se puede repetir el rango de selección).
# 3.Mostrar en pantalla (print()) el valor de cada número generado.
# 4.Sumar los 5 números generados y guardar el resultado en una variable.
# 5.Mostrar en pantalla el resultado de la suma con el mensaje:
# La suma de los números generados es: __

import random  # módulo para generar números al azar

# random() da un decimal entre 0.0 (incluido) y 1.0 (excluido)
# al multiplicar por 100 e int() queda un entero de 0 a 99
# Nota: las 5 usan el mismo "truco", no rangos distintos como pide la consigna
input_numero_1 = int(random.random() * 100)
input_numero_2 = int(random.random() * 100)
input_numero_3 = int(random.random() * 100)
input_numero_4 = int(random.random() * 100)
input_numero_5 = int(random.random() * 100)

print(f"El número 1 generado con random() es: {input_numero_1}")
print(f"El número 2 generado con random() es: {input_numero_2}")
print(f"El número 3 generado con random() es: {input_numero_3}")
print(f"El número 4 generado con random() es: {input_numero_4}")
print(f"El número 5 generado con random() es: {input_numero_5}")

# Sumamos las 5 variables y mostramos el total
input_suma = input_numero_1 + input_numero_2 + input_numero_3 + input_numero_4 + input_numero_5
print(f"La suma de los números generados es: {input_suma}")

# Misma idea en una lista: 5 enteros al azar entre 1 y 100 (ambos inclusive)
# "_" significa "no nos importa el índice, solo repetir 5 veces"
input_numeros = [random.randint(1, 100) for _ in range(5)]
print(f"Los números generados son: {input_numeros}")
input_suma = sum(input_numeros)  # suma todos los elementos de la lista
print(f"La suma de los números generados es: {input_suma}")

# Alternativa 1: 5 variables con random.randint() y un rango distinto en cada una.
# randint(a, b) incluye AMBOS extremos. Los intervalos no se pisan:
# 1-20, 21-40, 41-60, 61-80, 81-100

input_numero_1 = random.randint(1, 20)
input_numero_2 = random.randint(21, 40)
input_numero_3 = random.randint(41, 60)
input_numero_4 = random.randint(61, 80)
input_numero_5 = random.randint(81, 100)

print(f"El número 1 generado con randint() es: {input_numero_1}")
print(f"El número 2 generado con randint() es: {input_numero_2}")
print(f"El número 3 generado con randint() es: {input_numero_3}")
print(f"El número 4 generado con randint() es: {input_numero_4}")
print(f"El número 5 generado con randint() es: {input_numero_5}")

input_suma = input_numero_1 + input_numero_2 + input_numero_3 + input_numero_4 + input_numero_5
print(f"La suma de los números generados es: {input_suma}")

# Alternativa 2: 5 variables con random.randrange() y un rango distinto en cada una.
# randrange(a, b) es como range: incluye a y NO incluye b
# Por eso usamos 21, 41, 61... para llegar hasta 20, 40, 60, etc.

input_numero_1 = random.randrange(1, 21)
input_numero_2 = random.randrange(21, 41)
input_numero_3 = random.randrange(41, 61)
input_numero_4 = random.randrange(61, 81)
input_numero_5 = random.randrange(81, 101)

print(f"El número 1 generado con randrange() es: {input_numero_1}")
print(f"El número 2 generado con randrange() es: {input_numero_2}")
print(f"El número 3 generado con randrange() es: {input_numero_3}")
print(f"El número 4 generado con randrange() es: {input_numero_4}")
print(f"El número 5 generado con randrange() es: {input_numero_5}")

input_suma = input_numero_1 + input_numero_2 + input_numero_3 + input_numero_4 + input_numero_5
print(f"La suma de los números generados es: {input_suma}")

# Alternativa 3: 5 variables con random.choice() sobre conjuntos distintos.
# choice() elige UN elemento al azar de lo que le pasemos
# range(1, 21) genera 1..20; cada choice usa un range distinto (no se repite el conjunto)

input_numero_1 = random.choice(range(1, 21))
input_numero_2 = random.choice(range(21, 41))
input_numero_3 = random.choice(range(41, 61))
input_numero_4 = random.choice(range(61, 81))
input_numero_5 = random.choice(range(81, 101))

print(f"El número 1 generado con choice() es: {input_numero_1}")
print(f"El número 2 generado con choice() es: {input_numero_2}")
print(f"El número 3 generado con choice() es: {input_numero_3}")
print(f"El número 4 generado con choice() es: {input_numero_4}")
print(f"El número 5 generado con choice() es: {input_numero_5}")

input_suma = input_numero_1 + input_numero_2 + input_numero_3 + input_numero_4 + input_numero_5
print(f"La suma de los números generados es: {input_suma}")