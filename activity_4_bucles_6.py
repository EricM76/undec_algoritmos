# 📌 Consigna: 
# Desarrollar un programa que permita cargar un párrafo (texto) desde el teclado en una variable de 
# tipo carácter. El texto ingresado podrá contener cualquier carácter tales como:
# - números (‘2’, ‘36’, ‘52’, etc)
# - letras (‘A’, ’h’, ’L’, ’i’, etc)
# - símbolos especiales (‘!’, ’#’, ’ ’,  ‘-’, etc)
# Para procesar cada párrafo supondremos que: el carácter punto (‘.’) indica el final de una frase; 
# que cada palabra de ese párrafo está separada de las demás por un carácter de espacio en blanco (‘ ’); 
# y que al inicio el párrafo tendrá al menos una palabra por defecto. 
# Además, el programa debe realizar el siguiente procesamientos sobre la secuencia ingresada:
# - Mostrar el párrafo completo.
# - Mostrar el párrafo de atrás hacia adelante.
# - Determinar cuántas vocales tiene el párrafo.
# - Determinar cuántos caracteres tiene el párrafo.
# - Determinar cuántas palabras tiene el párrafo.
# - Determinar cuantas frases tiene el párrafo.
# Nota: normalizar el párrafo antes de procesarlo. Como variante en Python podrá recorrer el párrafo usando un ciclo for iterable.

parrafo = input("Ingrese un párrafo: ")

# Normalizar: minúsculas, sin espacios al inicio/final y sin espacios repetidos
parrafo = parrafo.strip().lower()
parrafo_normalizado = ""
espacio_anterior = False

for caracter in parrafo:
    if caracter == " ":
        if not espacio_anterior:
            parrafo_normalizado += caracter
        espacio_anterior = True
    else:
        parrafo_normalizado += caracter
        espacio_anterior = False

parrafo = parrafo_normalizado

print(f"Párrafo completo: {parrafo}")

parrafo_invertido = ""
for caracter in parrafo:
    parrafo_invertido = caracter + parrafo_invertido

print(f"Párrafo invertido: {parrafo_invertido}")

vocales = 0
caracteres = 0
palabras = 1  # el párrafo tiene al menos una palabra por defecto
frases = 0

for caracter in parrafo:
    caracteres += 1
    if caracter in "aeiouáéíóúü":
        vocales += 1
    if caracter == " ":
        palabras += 1
    if caracter == ".":
        frases += 1

print(f"Cantidad de vocales: {vocales}")
print(f"Cantidad de caracteres: {caracteres}")
print(f"Cantidad de palabras: {palabras}")
print(f"Cantidad de frases: {frases}")
