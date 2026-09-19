# 📌 Consigna:
#  
# Incorporar un menú de opciones al ejercicio anterior para que permitir al usuario seleccionar algunas de 
# las siguientes opciones:
# 1. Crear archivo: 
#   - Permite crear el archivo. En caso de que el archivo ya exista, advertir con un mensaje en pantalla al usuario y solicitar que indique si desea crearlo nuevamente.
# 2. Cargar registro de frases
#   - Permite cargar frases. La condición para el fin de la carga será el ingreso de la palabra “Fin”.
# 3. Mostrar listado de frases
#   - Muestra el listado de todas las frases en formato tabla.
# 4. Salir.

# Nota: implementar cada opción del menú por medio de funciones.

import os

NOMBRE_ARCHIVO = "archivoPython.dat"


def crear_archivo():
    if os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo ya existe.")
        respuesta = input("¿Desea crearlo nuevamente? (S/N): ")
        if respuesta.upper() != "S":
            print("No se creó el archivo.")
            return
    archivo = open(NOMBRE_ARCHIVO, "w")
    archivo.close()
    print("Archivo creado correctamente.")


def cargar_frases():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return

    archivo = open(NOMBRE_ARCHIVO, "a")
    frase = input("Ingrese una frase: ")
    while frase != "Fin":
        autor = input("Ingrese el autor de la frase: ")
        archivo.write(frase + " - " + autor + "\n")
        frase = input("Ingrese una frase: ")
    archivo.close()
    print("Frases cargadas correctamente.")


def mostrar_frases():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return

    archivo = open(NOMBRE_ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        print("No hay frases registradas.")
        return

    print("-" * 60)
    print(f"{'Frase':<40} {'Autor':<20}")
    print("-" * 60)
    for linea in lineas:
        linea = linea.strip()
        if " - " in linea:
            frase, autor = linea.rsplit(" - ", 1)
            print(f"{frase:<40} {autor:<20}")
        else:
            print(linea)
    print("-" * 60)


def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Crear archivo")
    print("2. Cargar registro de frases")
    print("3. Mostrar listado de frases")
    print("4. Salir")


# Programa principal
opcion = 0
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_archivo()
    elif opcion == 2:
        cargar_frases()
    elif opcion == 3:
        mostrar_frases()
    elif opcion == 4:
        print("Fin del programa.")
    else:
        print("Opción inválida.")
