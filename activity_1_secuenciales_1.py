# 📌 Consigna:
# Generar un algoritmo que permita calcular el área de un círculo utilizando la siguiente fórmula:
# Área = π * radio^2
# Donde π (pi) es una constante matemática aproximadamente igual a 3.14159.

# 📌 Requisitos:
# - El algoritmo debe solicitar al usuario ingresar el valor del radio del círculo.
# - Debe realizar el cálculo del área utilizando la fórmula proporcionada.
# - Debe mostrar el resultado del cálculo por pantalla.

# 📌 Ejemplo de ejecución:
# Ingrese el valor del radio del círculo: 5
# El área del círculo es: 78.53981633974483

input_radio = int(input("Ingrese el valor del radio del círculo: "))
area = 3.14159 * input_radio**2
print(f"El área del círculo es: {area}")