# 📌 Consigna:
# Generar un programa que permita cargar por teclado tres números enteros que se supone representan las edades de tres personas. 
# - Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en pantalla con un mensaje tal como: ‘Alguna es incorrecta: negativa’. 
# - Si todos los valores eran positivos o cero, informe que todas eran correctas con un mensaje tal como ‘Las edades son correctas’.
# - De manera adicional, y antes de finalizar, deberá determinar y mostrar en pantalla el menor número ingresado.

# Guardamos las 3 edades en una lista: [0] primera, [1] segunda, [2] tercera
input_edades = [
    int(input("Ingrese la edad de la primera persona: ")),
    int(input("Ingrese la edad de la segunda persona: ")),
    int(input("Ingrese la edad de la tercera persona: "))
    ]

# Con "or" alcanza con que UNA sea < 0 para marcarlas como incorrectas
# El 0 está permitido (la consigna: positivos o cero = correctas)
if input_edades[0] < 0 or input_edades[1] < 0 or input_edades[2] < 0:
    print("Alguna es incorrecta: negativa")
else:
    print("Las edades son correctas")

# Buscamos el menor comparando de a uno (sin usar min())
# Arrancamos suponiendo que el primero es el más chico
menor = input_edades[0]
if input_edades[1] < menor:
    menor = input_edades[1]  # la segunda es más chica: actualizamos
if input_edades[2] < menor:
    menor = input_edades[2]  # la tercera es más chica: actualizamos
print(f"El menor número ingresado es: {menor}")