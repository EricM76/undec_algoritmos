# 📌 Consigna:
#
# Necesitamos calcular la densidad de dos objetos.
#
# 1. Crear una función calcular_densidad(masa, volumen) que retorna la densidad (masa / volumen).
# 2. Usar la función para calcular la densidad de un objeto con:
#   - Masa = 10 kg y Volumen = 2 m³
#   - Masa = 270 kg y Volumen = 33 m³
# 3. Mostrar ambos resultados por consola.
# 4. Sumar ambas densidades y mostrar el resultado con el texto:
#
# La densidad total es: _____


# Densidad = masa / volumen. Recibe ambos valores y devuelve el resultado.
def calcular_densidad(masa, volumen):
    return masa / volumen


# Primer objeto: 10 kg / 2 m³
masa_1 = 10
volumen_1 = 2
densidad_1 = calcular_densidad(masa_1, volumen_1)
print(f"Objeto 1 - Masa: {masa_1} kg, Volumen: {volumen_1} m3, Densidad: {densidad_1:.2f}")

# Segundo objeto: 270 kg / 33 m³
masa_2 = 270
volumen_2 = 33
densidad_2 = calcular_densidad(masa_2, volumen_2)
print(f"Objeto 2 - Masa: {masa_2} kg, Volumen: {volumen_2} m3, Densidad: {densidad_2:.2f}")

# Suma de ambas densidades, con el texto pedido en la consigna
densidad_total = densidad_1 + densidad_2
print(f"La densidad total es: {densidad_total:.2f}")
