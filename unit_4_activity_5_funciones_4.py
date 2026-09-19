# 📌 Consigna:
# Desarrollar un programa que permita cargar y convertir una temperatura en grados Celsius (°C)
# (comprendida entre -500 y 15000) a su equivalente en grados Fahrenheit (°F). 
# 
# Deberá validarse que la temperatura ingresada se encuentre en el intervalo requerido antes de pasar a la 
# conversión de la misma. Tener en cuenta que el diseño debe implementar las siguientes funciones:
# - Función validaCelsius(): permite validar que la temperatura ingresada en °C se encuentre comprendida en el intervalo [-500, 15000] informando la situación con un mensaje en pantalla. Esta función recibe como argumento la temperatura ingresada y devuelve como valor de retorno una bandera que indique el resultado de la validación.
# Función convierteCaF() permite convertir la temperatura de °C a °F. Dicha función recibe como argumento la temperatura en °C y devuelve como valor de retorno la temperatura en °F. 
# 
# Recordamos que la fórmula matemática para convertir °C a °F es la siguiente:  °F = (°C * 9/5) + 32

CELSIUS_MIN = -500
CELSIUS_MAX = 15000


# Recibe la temperatura en °C y devuelve True si está en [-500, 15000], False si no.
# Informa en pantalla si la validación fue correcta o no.
def validaCelsius(celsius):
    if CELSIUS_MIN <= celsius <= CELSIUS_MAX:
        print("Temperatura válida.")
        return True
    else:
        print(f"Temperatura no válida. Debe estar entre {CELSIUS_MIN} y {CELSIUS_MAX} °C.")
        return False


# Convierte °C a °F con la fórmula: °F = (°C * 9/5) + 32
def convierteCaF(celsius):
    return (celsius * 9 / 5) + 32


# Cargamos la temperatura y validamos antes de convertir
celsius = float(input("Ingrese la temperatura en °C: "))
valida = validaCelsius(celsius)

# Mientras la bandera sea False, se pide de nuevo
while not valida:
    celsius = float(input("Ingrese la temperatura en °C: "))
    valida = validaCelsius(celsius)

fahrenheit = convierteCaF(celsius)
print(f"{celsius} °C equivalen a {fahrenheit} °F")

