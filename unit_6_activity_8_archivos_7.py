# 📌 Consigna:
#
# Desarrollar un programa para gestionar un archivo telefónico que contiene registros de los nombres y 
# teléfonos de los clientes de una empresa. El programa incorpora funciones para crear el archivo con el 
# listado si no existe, añadir el teléfono de un nuevo cliente y para consultar el teléfono de un cliente. 
# El listado debe estar guardado en el archivo listadoTel.dat con la siguiente estructura de registro.
# 
# Registro: telEmpleado
#   caracter: nombre
#   entero: nroTelefono
# finRegistro

import os

NOMBRE_ARCHIVO = "listadoTel.dat"


def crear_archivo():
    if os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo ya existe.")
        return

    archivo = open(NOMBRE_ARCHIVO, "w")
    archivo.close()
    print("Archivo creado correctamente.")


def anadir_cliente():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return

    nombre = input("Ingrese el nombre del cliente: ")
    nroTelefono = int(input("Ingrese el número de teléfono: "))

    archivo = open(NOMBRE_ARCHIVO, "a")
    archivo.write(nombre + " - " + str(nroTelefono) + "\n")
    archivo.close()
    print("Cliente añadido correctamente.")


def consultar_telefono():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return

    nombre_buscar = input("Ingrese el nombre del cliente a consultar: ")

    archivo = open(NOMBRE_ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    encontrado = False
    for linea in lineas:
        linea = linea.strip()
        if " - " in linea:
            nombre, nroTelefono = linea.rsplit(" - ", 1)
            if nombre == nombre_buscar:
                print("Teléfono de", nombre + ":", nroTelefono)
                encontrado = True
                break

    if not encontrado:
        print("Cliente no encontrado.")


def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Crear archivo")
    print("2. Añadir teléfono de un nuevo cliente")
    print("3. Consultar teléfono de un cliente")
    print("4. Salir")


# Programa principal
opcion = 0
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_archivo()
    elif opcion == 2:
        anadir_cliente()
    elif opcion == 3:
        consultar_telefono()
    elif opcion == 4:
        print("Fin del programa.")
    else:
        print("Opción inválida.")
