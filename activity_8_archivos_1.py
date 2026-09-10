# 📌 Consigna:
#
# Desarrollar un programa que permita generar un archivo llamado archivoPython.dat, guarde en el mismo 
# la frase “Mi primer archivo en Python” y luego muestre el contenido del archivo en pantalla.

# Generar el archivo.
archivo = open("archivoPython.dat", "w")
archivo.write("Mi primer archivo en Python")
archivo.close()

# Mostrar el contenido del archivo.
archivo = open("archivoPython.dat", "r")
print(archivo.read())
archivo.close()
