# 📌 Consigna: 
#
# Desarrollar un programa que permita agregar al registro de frases anterior, un nuevo campo que contenga 
# el autor de la frase.

# Abrir el archivo en modo escritura.
archivo = open("archivoPython.dat", "w")

# Pedir al usuario que ingrese las frases y sus autores.
frase = input("Ingrese una frase: ")
while frase != "Fin":
    autor = input("Ingrese el autor de la frase: ")
    archivo.write(frase + " - " + autor + "\n")
    frase = input("Ingrese una frase: ")

# Cerrar el archivo.
archivo.close()
