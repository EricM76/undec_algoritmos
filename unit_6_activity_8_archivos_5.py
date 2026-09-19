# 📌 Consigna:
#
# Desarrollar un programa que lea el archivo denominado unidadesAlgoritmo.dat (incluido como material 
# adicional para la actividad) y copie todo el contenido del archivo a otro denominado unidadesCopia.dat de 
# modo que queden los dos archivos exactamente iguales. Considerar que el archivo original fue creado con la 
# siguiente estructura de registro.

# Abrir el archivo original en modo lectura binaria.
origen = open("unidadesAlgoritmo.dat", "rb")
contenido = origen.read()
origen.close()

# Crear el archivo copia y escribir el mismo contenido.
destino = open("unidadesCopia.dat", "wb")
destino.write(contenido)
destino.close()

print("Archivo copiado correctamente.")
