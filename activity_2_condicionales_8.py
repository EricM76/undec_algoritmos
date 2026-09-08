# 📌 Consigna:
# Generar un programa que permita cargar por teclado tres números enteros que se supone representan las edades de tres personas. 
# - Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en pantalla con un mensaje tal como: ‘Alguna es incorrecta: negativa’. 
# - Si todos los valores eran positivos o cero, informe que todas eran correctas con un mensaje tal como ‘Las edades son correctas’.
# - De manera adicional, y antes de finalizar, deberá determinar y mostrar en pantalla el menor número ingresado.

input_edades = [
    int(input("Ingrese la edad de la primera persona: ")), 
    int(input("Ingrese la edad de la segunda persona: ")), 
    int(input("Ingrese la edad de la tercera persona: "))
    ]
if input_edades[0] < 0 or input_edades[1] < 0 or input_edades[2] < 0:
    print("Alguna es incorrecta: negativa")
else:
    print("Las edades son correctas")

menor = input_edades[0]
if input_edades[1] < menor:
    menor = input_edades[1]
if input_edades[2] < menor:
    menor = input_edades[2]
print(f"El menor número ingresado es: {menor}")