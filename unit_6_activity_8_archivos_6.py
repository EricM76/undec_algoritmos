# 📌 Consigna:
#
# Desarrollar un programa que solicite al usuario un número n comprendido entre 1 y 10 y guarde en un archivo 
# llamado tabla.dat, la tabla de multiplicar de n. La estructura del registro a almacenar en el archivo es la 
# siguiente.
# 
# Registro: tabla
#   caracter: nPor
#   entero: resultado
# finRegistro

# Solicitar el número n entre 1 y 10.
n = int(input("Ingrese un número entre 1 y 10: "))
while n < 1 or n > 10:
    print("Número inválido.")
    n = int(input("Ingrese un número entre 1 y 10: "))

# Crear el archivo y guardar la tabla de multiplicar.
archivo = open("tabla.dat", "w")
for i in range(1, 11):
    nPor = str(i) + "x" + str(n)
    resultado = i * n
    archivo.write(nPor + " - " + str(resultado) + "\n")
archivo.close()

print("Tabla de multiplicar guardada en tabla.dat")
