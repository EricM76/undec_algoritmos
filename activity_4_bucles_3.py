# 📌 Consigna: 
# Simular que cargamos las notas de 5 estudiantes.
# - Para cada estudiante, pedir al usuario una nota (entre 1 y 10).
# - Mostrar si aprobó o no (nota ≥ 6).
# - Al final, mostrar la cantidad de aprobados y desaprobados.
# 💡 Ejemplo de salida esperada:
# Nota del estudiante 1: 7 → Aprobado
# Nota del estudiante 2: 4 → Desaprobado
# ...
# Aprobados: 3
# Desaprobados: 2

aprobados = 0
desaprobados = 0

for i in range(1, 6):
    nota = int(input(f"Ingrese la nota del estudiante {i}: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")