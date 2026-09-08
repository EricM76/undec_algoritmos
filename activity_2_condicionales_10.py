# 📌 Consigna:
# Generar un programa para una asociación de vinicultores que tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que 
# entrega en un embarque, considerando lo siguiente: 
# - Si es de tipo A, se le cargan $200 al precio inicial cuando es de tamaño 1; y $300 si es de tamaño 2. 
# - Si es de tipo B, se rebajan $300 cuando es de tamaño 1, y $500 cuando es de tamaño 2. 
# Al finalizar de procesar los datos debe determinar la ganancia obtenida y mostrar el resultado.
# Nota: normalizar la cadena de caracteres correspondiente al tipo de uva antes de realizar las comparaciones.

input_tipo = input("Ingrese el tipo de uva: ").strip().upper()
input_tamaño = int(input("Ingrese el tamaño de la uva: "))
input_precio_inicial = int(input("Ingrese el precio inicial de la uva: "))
input_cantidad = int(input("Ingrese la cantidad de kilos de uva: "))

if input_tipo == "A":
    if input_tamaño == 1:
        input_precio_final = input_precio_inicial + 200
    elif input_tamaño == 2:
        input_precio_final = input_precio_inicial + 300
    else:
        print("El tamaño de la uva es incorrecto")
elif input_tipo == "B":
    if input_tamaño == 1:
        input_precio_final = input_precio_inicial - 300
    elif input_tamaño == 2:
        input_precio_final = input_precio_inicial - 500
    else:
        print("El tamaño de la uva es incorrecto")
else:
    print("El tipo de uva es incorrecto")

if input_tipo == "A" or input_tipo == "B":
    if input_tamaño == 1 or input_tamaño == 2:
        input_ganancia = input_precio_final * input_cantidad
        print(f"La ganancia obtenida es: {input_ganancia}")

# Alternativa 2 del algoritmo 10: tabla de ajustes con un diccionario.

input_tipo = input("Ingrese el tipo de uva: ").strip().upper()
input_tamaño = int(input("Ingrese el tamaño de la uva: "))
input_precio_inicial = int(input("Ingrese el precio inicial de la uva: "))
input_cantidad = int(input("Ingrese la cantidad de kilos de uva: "))

input_ajustes = {
    ("A", 1): 200,
    ("A", 2): 300,
    ("B", 1): -300,
    ("B", 2): -500,
}

if (input_tipo, input_tamaño) in input_ajustes:
    input_precio_final = input_precio_inicial + input_ajustes[(input_tipo, input_tamaño)]
    input_ganancia = input_precio_final * input_cantidad
    print(f"La ganancia obtenida es: {input_ganancia}")
else:
    print("El tipo o el tamaño de la uva es incorrecto")