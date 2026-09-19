# 📌 Consigna:
#  Dado un listado de animales en una veterinaria, separarlos en salvajes y domésticos.
# animales = ["perro", "gato", "tigre", "león", "conejo", "jirafa", "elefante"]
#
# Pasos:
# 1. Usar pop() para extraer los domésticos y almacenarlos en otra lista.
# 2. Lo mismo con los salvajes.
# 3. Ordenar ambas listas alfabéticamente.
# 4. Mostrar ambas listas por consola.

animales = ["perro", "gato", "tigre", "león", "conejo", "jirafa", "elefante"]
domesticos = []
salvajes = []

# 1 y 2. Extraer cada animal con pop() y clasificarlo de forma interactiva.
while len(animales) > 0:
    print(f"\nAnimales restantes: {animales}")
    animal = animales.pop(0)
    tipo = input(f"¿{animal} es doméstico (d) o salvaje (s)?: ").strip().lower()

    while tipo not in ("d", "s"):
        tipo = input("Respuesta inválida. Ingrese d (doméstico) o s (salvaje): ").strip().lower()

    if tipo == "d":
        domesticos.append(animal)
    else:
        salvajes.append(animal)

# 3. Ordenar ambas listas alfabéticamente.
domesticos.sort()
salvajes.sort()

# 4. Mostrar ambas listas por consola.
print(f"\nAnimales domésticos: {domesticos}")
print(f"Animales salvajes: {salvajes}")
