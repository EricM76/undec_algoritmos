# 📌 Consigna:
# Crea un programa que permita agregar nombres de estudiantes como claves y sus calificaciones como valores en un diccionario 
# ( La cantidad de estudiantes a cargar en el diccionario se solicita al inicio).
# Luego, imprime el diccionario.

# Crear una variable llamada estudiantes y asignarle un diccionario vacío.
estudiantes = {}

# Solicitar la cantidad de estudiantes a cargar en el diccionario.
cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes a cargar en el diccionario: "))

# Crear un bucle for para agregar los nombres de los estudiantes y sus calificaciones al diccionario.
for i in range(cantidadEstudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    estudiantes[nombre] = calificacion

# Imprimir el diccionario.
print(estudiantes)