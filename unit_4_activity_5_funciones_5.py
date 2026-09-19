#📌 Consigna: 
# Desarrollar un programa que utilizando una función llamada cubo() permita calcular el cubo de un número real. 
# Antes de invocarla para obtener el resultado, se debe validar que el número ingresado por el usuario sea de 
# tipo real utilizando una función llamada validaReal(). Aclaramos que cuando el número ingresado no sea real 
# se debe volver a solicitar y validar hasta que cumpla con lo requerido.


# Recibe el valor ingresado (texto) y devuelve True si se puede convertir a número real, False si no.
# Informa en pantalla si la validación fue correcta o no.
def validaReal(valor):
    try:
        float(valor)
        print("Número real válido.")
        return True
    except ValueError:
        print("El valor ingresado no es un número real. Intente de nuevo.")
        return False


# Calcula el cubo de un número real: n³
def cubo(numero):
    return numero ** 3


# Pedimos el número y validamos que sea real antes de calcular el cubo
entrada = input("Ingrese un número real: ")
valida = validaReal(entrada)

# Mientras la bandera sea False, se pide de nuevo
while not valida:
    entrada = input("Ingrese un número real: ")
    valida = validaReal(entrada)

numero = float(entrada)
resultado = cubo(numero)
print(f"El cubo de {numero} es {resultado}")
