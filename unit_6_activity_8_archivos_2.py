# 📌 Consigna: 
#
# Supongamos que deseamos modificar el ejercicio anterior para permitir al usuario añadir varias frases al 
# archivo y finalizar cuando se ingrese “Fin”, desarrolle el programa correspondiente.

# Abrir el archivo en modo escritura.
archivo = open("archivoPython.dat", "w")

# Pedir al usuario que ingrese las frases.
frase = input("Ingrese una frase: ")
while frase != "Fin":
    archivo.write(frase + "\n")
    frase = input("Ingrese una frase: ")

# Cerrar el archivo.
archivo.close()