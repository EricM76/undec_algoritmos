# 📌 Consigna:
#
# Una fábrica de alimentos envasados ha solicitado el desarrollo de un programa que permita almacenar en un 
# archivo secuencial llamado empleadosAltas.dat, registros  con información sobre cada uno de sus empleados.
# 
# Registro: empleado
#   entero: legajo
#   caracter: apellido
#   caracter: nombre
#   entero: dni
#   entero: edad
#   entero: sueldo
# finRegistro
#
# Se solicita desarrollar un programa que permita manipular el archivo de empleados por medio de menú con las 
# siguientes opciones:
#
# 1. Crear el archivo.
#   - Permite crear el archivo. En caso de que el archivo ya exista advertir con un mensaje en pantalla al 
#     usuario y solicitar que se indique si desea crearlo nuevamente.
# 2. Cargar registro de empleados.
#   - Permite cargar registros de empleados de manera ordenada. 
#   - La condición de fin de carga será un legajo cuyo número sea igual a cero.
# 3. Consultar registro de empleados.
#   - Muestra información de un empleado.
#   - La búsqueda de un empleado se debe hacer usando como campo clave el legajo.
# 4. Mostrar listado de empleados en forma de tabla.
#   - Muestra el listado de todos los empleados en forma de tabla.
# 6. Modificar registro de empleados.
#   - Permite modificar campos correspondientes a la dirección, sueldo y antigüedad de un registro de empleados. 
#   - Para la búsqueda del empleado a modificar, se utilizará como campo clave el legajo.
# 7. Borrar registro de empleados.
#   - Permite borrar un registro de empleado. 
#   - Para la búsqueda del empleado a eliminar se usará como campo clave el legajo.
# 8. Calcular el monto total de sueldos.
#   - Permite calcular el monto total que debe pagar la empresa por mes. 
#   - El resultado debe mostrarse por pantalla.
# 9. Salir.
#   - Permite salir del programa.
# Nota: Implementar el menú a través de funciones.

import os

NOMBRE_ARCHIVO = "empleadosAltas.dat"


def parsear_linea(linea):
    """Convierte una línea del archivo en un diccionario de empleado."""
    partes = linea.strip().split(" - ")
    if len(partes) != 6:
        return None
    return {
        "legajo": int(partes[0]),
        "apellido": partes[1],
        "nombre": partes[2],
        "dni": int(partes[3]),
        "edad": int(partes[4]),
        "sueldo": int(partes[5]),
    }


def formatear_empleado(emp):
    """Convierte un diccionario de empleado en una línea para el archivo."""
    return (
        str(emp["legajo"]) + " - "
        + emp["apellido"] + " - "
        + emp["nombre"] + " - "
        + str(emp["dni"]) + " - "
        + str(emp["edad"]) + " - "
        + str(emp["sueldo"]) + "\n"
    )


def leer_empleados():
    """Lee todos los empleados del archivo y los devuelve en una lista."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        return None

    archivo = open(NOMBRE_ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    empleados = []
    for linea in lineas:
        emp = parsear_linea(linea)
        if emp is not None:
            empleados.append(emp)
    return empleados


def guardar_empleados(empleados):
    """Guarda la lista de empleados en el archivo, reemplazando el contenido."""
    archivo = open(NOMBRE_ARCHIVO, "w")
    for emp in empleados:
        archivo.write(formatear_empleado(emp))
    archivo.close()


def archivo_existe_o_avisar():
    """Verifica si el archivo existe. Si no, avisa al usuario y retorna False."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return False
    return True


def crear_archivo():
    """Crea el archivo de empleados. Si ya existe, pregunta si se recrea."""
    if os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo ya existe.")
        respuesta = input("¿Desea crearlo nuevamente? (s/n): ").lower()
        if respuesta != "s":
            print("Operación cancelada.")
            return

    archivo = open(NOMBRE_ARCHIVO, "w")
    archivo.close()
    print("Archivo creado correctamente.")


def cargar_empleados():
    """Carga empleados de forma ordenada por legajo. Finaliza con legajo 0."""
    if not archivo_existe_o_avisar():
        return

    empleados = leer_empleados()

    print("Carga de empleados (legajo 0 para finalizar).")
    legajo = int(input("Ingrese legajo: "))

    while legajo != 0:
        # Verificar legajo duplicado
        existe = False
        for emp in empleados:
            if emp["legajo"] == legajo:
                existe = True
                break

        if existe:
            print("Ya existe un empleado con ese legajo.")
        else:
            apellido = input("Ingrese apellido: ")
            nombre = input("Ingrese nombre: ")
            dni = int(input("Ingrese DNI: "))
            edad = int(input("Ingrese edad: "))
            sueldo = int(input("Ingrese sueldo: "))

            nuevo = {
                "legajo": legajo,
                "apellido": apellido,
                "nombre": nombre,
                "dni": dni,
                "edad": edad,
                "sueldo": sueldo,
            }

            # Insertar de manera ordenada por legajo
            insertado = False
            for i in range(len(empleados)):
                if nuevo["legajo"] < empleados[i]["legajo"]:
                    empleados.insert(i, nuevo)
                    insertado = True
                    break
            if not insertado:
                empleados.append(nuevo)

            print("Empleado cargado correctamente.")

        legajo = int(input("Ingrese legajo: "))

    guardar_empleados(empleados)
    print("Carga finalizada.")


def consultar_empleado():
    """Busca un empleado por legajo y muestra sus datos."""
    if not archivo_existe_o_avisar():
        return

    empleados = leer_empleados()
    legajo = int(input("Ingrese el legajo a consultar: "))

    encontrado = False
    for emp in empleados:
        if emp["legajo"] == legajo:
            print("\n--- Datos del empleado ---")
            print("Legajo:", emp["legajo"])
            print("Apellido:", emp["apellido"])
            print("Nombre:", emp["nombre"])
            print("DNI:", emp["dni"])
            print("Edad:", emp["edad"])
            print("Sueldo:", emp["sueldo"])
            encontrado = True
            break

    if not encontrado:
        print("Empleado no encontrado.")


def mostrar_listado():
    """Muestra todos los empleados en forma de tabla."""
    if not archivo_existe_o_avisar():
        return

    empleados = leer_empleados()

    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    print("\n--- Listado de empleados ---")
    print(
        "Legajo".ljust(10)
        + "Apellido".ljust(15)
        + "Nombre".ljust(15)
        + "DNI".ljust(12)
        + "Edad".ljust(8)
        + "Sueldo".ljust(10)
    )
    print("-" * 70)

    for emp in empleados:
        print(
            str(emp["legajo"]).ljust(10)
            + emp["apellido"].ljust(15)
            + emp["nombre"].ljust(15)
            + str(emp["dni"]).ljust(12)
            + str(emp["edad"]).ljust(8)
            + str(emp["sueldo"]).ljust(10)
        )


def modificar_empleado():
    """Modifica la edad y el sueldo de un empleado buscado por legajo."""
    if not archivo_existe_o_avisar():
        return

    empleados = leer_empleados()
    legajo = int(input("Ingrese el legajo del empleado a modificar: "))

    encontrado = False
    for emp in empleados:
        if emp["legajo"] == legajo:
            print("Empleado encontrado:", emp["apellido"] + ",", emp["nombre"])
            emp["edad"] = int(input("Ingrese nueva edad: "))
            emp["sueldo"] = int(input("Ingrese nuevo sueldo: "))
            encontrado = True
            break

    if encontrado:
        guardar_empleados(empleados)
        print("Empleado modificado correctamente.")
    else:
        print("Empleado no encontrado.")


def borrar_empleado():
    """Elimina un empleado del archivo buscándolo por legajo."""
    if not archivo_existe_o_avisar():
        return

    empleados = leer_empleados()
    legajo = int(input("Ingrese el legajo del empleado a borrar: "))

    nuevos = []
    encontrado = False
    for emp in empleados:
        if emp["legajo"] == legajo:
            encontrado = True
        else:
            nuevos.append(emp)

    if encontrado:
        guardar_empleados(nuevos)
        print("Empleado borrado correctamente.")
    else:
        print("Empleado no encontrado.")


def calcular_total_sueldos():
    """Calcula y muestra el monto total de sueldos a pagar por mes."""
    if not archivo_existe_o_avisar():
        return

    empleados = leer_empleados()
    total = 0
    for emp in empleados:
        total = total + emp["sueldo"]

    print("Monto total de sueldos a pagar por mes:", total)


def mostrar_menu():
    """Muestra el menú de opciones del programa."""
    print("\n--- Menú de opciones ---")
    print("1. Crear el archivo")
    print("2. Cargar registro de empleados")
    print("3. Consultar registro de empleados")
    print("4. Mostrar listado de empleados")
    print("6. Modificar registro de empleados")
    print("7. Borrar registro de empleados")
    print("8. Calcular el monto total de sueldos")
    print("9. Salir")


# Programa principal
opcion = 0
while opcion != 9:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_archivo()
    elif opcion == 2:
        cargar_empleados()
    elif opcion == 3:
        consultar_empleado()
    elif opcion == 4:
        mostrar_listado()
    elif opcion == 6:
        modificar_empleado()
    elif opcion == 7:
        borrar_empleado()
    elif opcion == 8:
        calcular_total_sueldos()
    elif opcion == 9:
        print("Fin del programa.")
    else:
        print("Opción inválida.")
