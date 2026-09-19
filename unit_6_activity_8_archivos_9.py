# 📌 Consigna:
#
# El nuevo director de la Escuela de Ingeniería ha solicitado a los profesores de las diversas carreras y 
# asignaturas información referida al rendimiento académico de los estudiantes durante el año de cursado. 
# Se desea automatizar la carga para permitir a cada docente generar un archivo llamado alumnosAlta.dat con el siguiente registro 
# de información de cada alumno: 
# 
# Registro: alumno
#   entero: matricula
#   caracter: apellido
#   caracter: nombre
#   entero: edad
#   caracter: condicion
#   real: parcial1
#   real: parcial2
#   real: parcial3
# finRegistro
#
#demás se debe tener en cuenta que para cada archivo generado el primer registro será un registro único con la 
# siguiente información:
#
# Registro: asignatura
#   caracter: carrera
#   caracter: asignatura
#   entero: año
# finRegistro
#
# La cantidad de alumnos indicada en el primer registro del archivo deberá ser usada como control de carga del 
# número de registros de los alumnos. Diseñar un programa que permita realizar las siguientes operaciones: 
# 1. Crear el archivo.
#   - Permite crear el archivo. En caso de que el archivo ya exista advertir con un mensaje en pantalla al 
#     usuario y solicitar que indique si desea crearlo nuevamente. 
# 2. Cargar registros de alumnos. 
#   - Permite cargar registros de alumnos de manera ordenada. La condición para el fin de carga será una 
#     matrícula igual a cero o cuando se hayan cargado todos los registros indicados. 
# 3. Consultar registro de alumno.
#   - Muestra la información de un alumno. Para la búsqueda del alumno se debe usar como campo clave la 
#     matrícula.
# 4. Mostrar listado de alumnos en formato tabla.
#   - Muestra el listado de todos los alumnos en formato tabla. 
# 5. Modificar registro de alumno.
#   - Permite modificar los campos correspondientes a las notas de parciales del alumno. Para la búsqueda del 
#     alumno a modificar usar como campo clave la matrícula. 
# 6. Borrar registro de alumno.
#   - Permite dar de baja a un alumno. Para la búsqueda y baja posterior se deberá solicitar como campo clave la 
#     matrícula.
#   - Luego de eliminar el alumno deseado del archivo original se deberá copiar el mismo en otro archivo llamado 
#     alumnosBaja.dat. 
# 7. Calcular promedios.
#   - A partir del archivo aumnosAlta.dat generar un archivo llamado alumnosPromedio.dat que contenga información 
#     referida al promedio obtenido por cada alumno: MATRÍCULA, PROMEDIO. 
#   - Mostrar en pantalla la información generada aplicando algún formato de salida que facilite la lectura de la 
#     información. 
# 8. Mayor y menor promedio.
#   - A partir de los archivos generados determinar el alumno con mayor y menor promedio y mostrar en pantalla 
#     la información aplicando algún formato de salida que facilite la lectura de la información. 
# 9. Aprobados y desaprobados.
#   - A partir del archivo alumnosPromedio.dat, generar dos archivos adicionales aprobados.dat y desaprobados.dat
#     con la siguiente información: NOMBRE, APELLIDO, NOTAFINAL. 
# 10. Ordenar por edad.
#   - Leer el contenido del archivo alumnosAlta.dat y generar un archivo de salida con los alumnos ordenados por 
#     edad. Mostrar el resultado en pantalla. 
# 11. Ordenar por promedio.
#   - Leer el contenido del archivo alumnosAlta.dat y generar un archivo de salida con los alumnos ordenados por 
#     promedio.
# 12. Mostrar el resultado en pantalla. 
#
# Nota: implementar cada opción del menú por medio de funciones 

import os

ARCHIVO_ALTA = "alumnosAlta.dat"
ARCHIVO_BAJA = "alumnosBaja.dat"
ARCHIVO_PROMEDIO = "alumnosPromedio.dat"
ARCHIVO_APROBADOS = "aprobados.dat"
ARCHIVO_DESAPROBADOS = "desaprobados.dat"
ARCHIVO_POR_EDAD = "alumnosPorEdad.dat"
ARCHIVO_POR_PROMEDIO = "alumnosPorPromedio.dat"
NOTA_APROBACION = 6


def promedio_alumno(alumno):
    """Calcula el promedio de los tres parciales de un alumno."""
    return (alumno["parcial1"] + alumno["parcial2"] + alumno["parcial3"]) / 3


def formatear_asignatura(asig):
    """Convierte el registro de asignatura en una línea de archivo."""
    return (
        asig["carrera"] + " - "
        + asig["asignatura"] + " - "
        + str(asig["anio"]) + " - "
        + str(asig["cantidad"]) + "\n"
    )


def formatear_alumno(alumno):
    """Convierte un diccionario de alumno en una línea de archivo."""
    return (
        str(alumno["matricula"]) + " - "
        + alumno["apellido"] + " - "
        + alumno["nombre"] + " - "
        + str(alumno["edad"]) + " - "
        + alumno["condicion"] + " - "
        + str(alumno["parcial1"]) + " - "
        + str(alumno["parcial2"]) + " - "
        + str(alumno["parcial3"]) + "\n"
    )


def parsear_asignatura(linea):
    """Convierte la primera línea del archivo en el registro de asignatura."""
    partes = linea.strip().split(" - ")
    if len(partes) != 4:
        return None
    return {
        "carrera": partes[0],
        "asignatura": partes[1],
        "anio": int(partes[2]),
        "cantidad": int(partes[3]),
    }


def parsear_alumno(linea):
    """Convierte una línea del archivo en un diccionario de alumno."""
    partes = linea.strip().split(" - ")
    if len(partes) != 8:
        return None
    return {
        "matricula": int(partes[0]),
        "apellido": partes[1],
        "nombre": partes[2],
        "edad": int(partes[3]),
        "condicion": partes[4],
        "parcial1": float(partes[5]),
        "parcial2": float(partes[6]),
        "parcial3": float(partes[7]),
    }


def leer_archivo_alta():
    """Lee asignatura y alumnos desde alumnosAlta.dat. Retorna (asignatura, lista) o (None, None)."""
    if not os.path.exists(ARCHIVO_ALTA):
        return None, None

    archivo = open(ARCHIVO_ALTA, "r")
    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        return None, []

    asignatura = parsear_asignatura(lineas[0])
    alumnos = []
    for i in range(1, len(lineas)):
        alumno = parsear_alumno(lineas[i])
        if alumno is not None:
            alumnos.append(alumno)
    return asignatura, alumnos


def guardar_archivo_alta(asignatura, alumnos):
    """Guarda el registro de asignatura y la lista de alumnos en alumnosAlta.dat."""
    archivo = open(ARCHIVO_ALTA, "w")
    archivo.write(formatear_asignatura(asignatura))
    for alumno in alumnos:
        archivo.write(formatear_alumno(alumno))
    archivo.close()


def archivo_alta_existe_o_avisar():
    """Verifica si existe alumnosAlta.dat. Si no, avisa y retorna False."""
    if not os.path.exists(ARCHIVO_ALTA):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return False
    return True


def crear_archivo():
    """Crea el archivo alumnosAlta.dat. Si ya existe, pregunta si se recrea."""
    if os.path.exists(ARCHIVO_ALTA):
        print("El archivo ya existe.")
        respuesta = input("¿Desea crearlo nuevamente? (s/n): ").lower()
        if respuesta != "s":
            print("Operación cancelada.")
            return

    archivo = open(ARCHIVO_ALTA, "w")
    archivo.close()
    print("Archivo creado correctamente.")


def cargar_alumnos():
    """Carga alumnos ordenados por matrícula hasta completar la cantidad o matrícula 0."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()

    if asignatura is None:
        print("Ingrese los datos de la asignatura (primer registro):")
        carrera = input("Carrera: ")
        nombre_asig = input("Asignatura: ")
        anio = int(input("Año: "))
        cantidad = int(input("Cantidad de alumnos a cargar: "))
        asignatura = {
            "carrera": carrera,
            "asignatura": nombre_asig,
            "anio": anio,
            "cantidad": cantidad,
        }
        alumnos = []

    cargados = len(alumnos)
    if cargados >= asignatura["cantidad"]:
        print("Ya se cargó la cantidad máxima de alumnos indicada:", asignatura["cantidad"])
        return

    print("Carga de alumnos (matrícula 0 para finalizar).")
    print("Restan cargar:", asignatura["cantidad"] - cargados)

    matricula = int(input("Ingrese matrícula: "))

    while matricula != 0 and len(alumnos) < asignatura["cantidad"]:
        existe = False
        for alumno in alumnos:
            if alumno["matricula"] == matricula:
                existe = True
                break

        if existe:
            print("Ya existe un alumno con esa matrícula.")
        else:
            apellido = input("Ingrese apellido: ")
            nombre = input("Ingrese nombre: ")
            edad = int(input("Ingrese edad: "))
            condicion = input("Ingrese condición: ")
            parcial1 = float(input("Ingrese nota parcial 1: "))
            parcial2 = float(input("Ingrese nota parcial 2: "))
            parcial3 = float(input("Ingrese nota parcial 3: "))

            nuevo = {
                "matricula": matricula,
                "apellido": apellido,
                "nombre": nombre,
                "edad": edad,
                "condicion": condicion,
                "parcial1": parcial1,
                "parcial2": parcial2,
                "parcial3": parcial3,
            }

            insertado = False
            for i in range(len(alumnos)):
                if nuevo["matricula"] < alumnos[i]["matricula"]:
                    alumnos.insert(i, nuevo)
                    insertado = True
                    break
            if not insertado:
                alumnos.append(nuevo)

            print("Alumno cargado correctamente.")

        if len(alumnos) >= asignatura["cantidad"]:
            print("Se alcanzó la cantidad máxima de alumnos.")
            break

        matricula = int(input("Ingrese matrícula: "))

    guardar_archivo_alta(asignatura, alumnos)
    print("Carga finalizada.")


def consultar_alumno():
    """Busca un alumno por matrícula y muestra sus datos."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None:
        print("El archivo no tiene datos cargados.")
        return

    matricula = int(input("Ingrese la matrícula a consultar: "))

    encontrado = False
    for alumno in alumnos:
        if alumno["matricula"] == matricula:
            print("\n--- Datos del alumno ---")
            print("Matrícula:", alumno["matricula"])
            print("Apellido:", alumno["apellido"])
            print("Nombre:", alumno["nombre"])
            print("Edad:", alumno["edad"])
            print("Condición:", alumno["condicion"])
            print("Parcial 1:", alumno["parcial1"])
            print("Parcial 2:", alumno["parcial2"])
            print("Parcial 3:", alumno["parcial3"])
            encontrado = True
            break

    if not encontrado:
        print("Alumno no encontrado.")


def mostrar_listado():
    """Muestra la asignatura y el listado de alumnos en formato tabla."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None:
        print("El archivo no tiene datos cargados.")
        return

    print("\n--- Datos de la asignatura ---")
    print("Carrera:", asignatura["carrera"])
    print("Asignatura:", asignatura["asignatura"])
    print("Año:", asignatura["anio"])
    print("Cantidad prevista:", asignatura["cantidad"])

    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    print("\n--- Listado de alumnos ---")
    print(
        "Matrícula".ljust(12)
        + "Apellido".ljust(15)
        + "Nombre".ljust(15)
        + "Edad".ljust(6)
        + "Condición".ljust(12)
        + "P1".ljust(8)
        + "P2".ljust(8)
        + "P3".ljust(8)
    )
    print("-" * 84)

    for alumno in alumnos:
        print(
            str(alumno["matricula"]).ljust(12)
            + alumno["apellido"].ljust(15)
            + alumno["nombre"].ljust(15)
            + str(alumno["edad"]).ljust(6)
            + alumno["condicion"].ljust(12)
            + str(alumno["parcial1"]).ljust(8)
            + str(alumno["parcial2"]).ljust(8)
            + str(alumno["parcial3"]).ljust(8)
        )


def modificar_alumno():
    """Modifica las notas de parciales de un alumno buscado por matrícula."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None:
        print("El archivo no tiene datos cargados.")
        return

    matricula = int(input("Ingrese la matrícula del alumno a modificar: "))

    encontrado = False
    for alumno in alumnos:
        if alumno["matricula"] == matricula:
            print("Alumno encontrado:", alumno["apellido"] + ",", alumno["nombre"])
            alumno["parcial1"] = float(input("Ingrese nueva nota parcial 1: "))
            alumno["parcial2"] = float(input("Ingrese nueva nota parcial 2: "))
            alumno["parcial3"] = float(input("Ingrese nueva nota parcial 3: "))
            encontrado = True
            break

    if encontrado:
        guardar_archivo_alta(asignatura, alumnos)
        print("Alumno modificado correctamente.")
    else:
        print("Alumno no encontrado.")


def borrar_alumno():
    """Da de baja un alumno: lo quita de alta y lo copia en alumnosBaja.dat."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None:
        print("El archivo no tiene datos cargados.")
        return

    matricula = int(input("Ingrese la matrícula del alumno a dar de baja: "))

    nuevos = []
    eliminado = None
    for alumno in alumnos:
        if alumno["matricula"] == matricula:
            eliminado = alumno
        else:
            nuevos.append(alumno)

    if eliminado is None:
        print("Alumno no encontrado.")
        return

    archivo_baja = open(ARCHIVO_BAJA, "a")
    archivo_baja.write(formatear_alumno(eliminado))
    archivo_baja.close()

    asignatura["cantidad"] = max(0, asignatura["cantidad"] - 1)
    guardar_archivo_alta(asignatura, nuevos)
    print("Alumno dado de baja y copiado en", ARCHIVO_BAJA)


def calcular_promedios():
    """Genera alumnosPromedio.dat con matrícula y promedio, y lo muestra en pantalla."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None or len(alumnos) == 0:
        print("No hay alumnos para calcular promedios.")
        return

    archivo = open(ARCHIVO_PROMEDIO, "w")
    print("\n--- Promedios de alumnos ---")
    print("Matrícula".ljust(12) + "Promedio".ljust(10))
    print("-" * 22)

    for alumno in alumnos:
        prom = promedio_alumno(alumno)
        archivo.write(str(alumno["matricula"]) + " - " + str(round(prom, 2)) + "\n")
        print(str(alumno["matricula"]).ljust(12) + str(round(prom, 2)).ljust(10))

    archivo.close()
    print("Archivo", ARCHIVO_PROMEDIO, "generado correctamente.")


def mayor_menor_promedio():
    """Determina y muestra el alumno con mayor y menor promedio."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None or len(alumnos) == 0:
        print("No hay alumnos cargados.")
        return

    mayor = alumnos[0]
    menor = alumnos[0]
    prom_mayor = promedio_alumno(mayor)
    prom_menor = promedio_alumno(menor)

    for alumno in alumnos:
        prom = promedio_alumno(alumno)
        if prom > prom_mayor:
            mayor = alumno
            prom_mayor = prom
        if prom < prom_menor:
            menor = alumno
            prom_menor = prom

    print("\n--- Mayor promedio ---")
    print("Matrícula:", mayor["matricula"])
    print("Nombre:", mayor["nombre"], mayor["apellido"])
    print("Promedio:", round(prom_mayor, 2))

    print("\n--- Menor promedio ---")
    print("Matrícula:", menor["matricula"])
    print("Nombre:", menor["nombre"], menor["apellido"])
    print("Promedio:", round(prom_menor, 2))


def generar_aprobados_desaprobados():
    """Genera aprobados.dat y desaprobados.dat con nombre, apellido y nota final."""
    if not archivo_alta_existe_o_avisar():
        return

    if not os.path.exists(ARCHIVO_PROMEDIO):
        print("Primero debe calcular los promedios (opción 7).")
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None or len(alumnos) == 0:
        print("No hay alumnos cargados.")
        return

    # Índice de alumnos por matrícula
    por_matricula = {}
    for alumno in alumnos:
        por_matricula[alumno["matricula"]] = alumno

    archivo_prom = open(ARCHIVO_PROMEDIO, "r")
    lineas = archivo_prom.readlines()
    archivo_prom.close()

    archivo_apr = open(ARCHIVO_APROBADOS, "w")
    archivo_des = open(ARCHIVO_DESAPROBADOS, "w")

    cantidad_apr = 0
    cantidad_des = 0

    for linea in lineas:
        partes = linea.strip().split(" - ")
        if len(partes) != 2:
            continue
        matricula = int(partes[0])
        promedio = float(partes[1])

        if matricula not in por_matricula:
            continue

        alumno = por_matricula[matricula]
        registro = alumno["nombre"] + " - " + alumno["apellido"] + " - " + str(promedio) + "\n"

        if promedio >= NOTA_APROBACION:
            archivo_apr.write(registro)
            cantidad_apr = cantidad_apr + 1
        else:
            archivo_des.write(registro)
            cantidad_des = cantidad_des + 1

    archivo_apr.close()
    archivo_des.close()

    print("Archivos generados correctamente.")
    print("Aprobados:", cantidad_apr, "->", ARCHIVO_APROBADOS)
    print("Desaprobados:", cantidad_des, "->", ARCHIVO_DESAPROBADOS)


def ordenar_por_edad():
    """Genera un archivo con alumnos ordenados por edad y lo muestra en pantalla."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None or len(alumnos) == 0:
        print("No hay alumnos cargados.")
        return

    ordenados = list(alumnos)
    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            if ordenados[j]["edad"] < ordenados[i]["edad"]:
                aux = ordenados[i]
                ordenados[i] = ordenados[j]
                ordenados[j] = aux

    archivo = open(ARCHIVO_POR_EDAD, "w")
    archivo.write(formatear_asignatura(asignatura))
    for alumno in ordenados:
        archivo.write(formatear_alumno(alumno))
    archivo.close()

    print("\n--- Alumnos ordenados por edad ---")
    print("Matrícula".ljust(12) + "Apellido".ljust(15) + "Nombre".ljust(15) + "Edad".ljust(6))
    print("-" * 48)
    for alumno in ordenados:
        print(
            str(alumno["matricula"]).ljust(12)
            + alumno["apellido"].ljust(15)
            + alumno["nombre"].ljust(15)
            + str(alumno["edad"]).ljust(6)
        )
    print("Archivo", ARCHIVO_POR_EDAD, "generado correctamente.")


def ordenar_por_promedio():
    """Genera un archivo con alumnos ordenados por promedio."""
    if not archivo_alta_existe_o_avisar():
        return

    asignatura, alumnos = leer_archivo_alta()
    if asignatura is None or len(alumnos) == 0:
        print("No hay alumnos cargados.")
        return

    ordenados = list(alumnos)
    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            if promedio_alumno(ordenados[j]) < promedio_alumno(ordenados[i]):
                aux = ordenados[i]
                ordenados[i] = ordenados[j]
                ordenados[j] = aux

    archivo = open(ARCHIVO_POR_PROMEDIO, "w")
    archivo.write(formatear_asignatura(asignatura))
    for alumno in ordenados:
        archivo.write(formatear_alumno(alumno))
    archivo.close()

    print("Archivo", ARCHIVO_POR_PROMEDIO, "generado correctamente.")
    print("Use la opción 12 para ver el resultado en pantalla.")


def mostrar_ordenados_por_promedio():
    """Muestra en pantalla el archivo de alumnos ordenados por promedio."""
    if not os.path.exists(ARCHIVO_POR_PROMEDIO):
        print("Primero debe ordenar por promedio (opción 11).")
        return

    archivo = open(ARCHIVO_POR_PROMEDIO, "r")
    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        print("El archivo está vacío.")
        return

    asignatura = parsear_asignatura(lineas[0])
    print("\n--- Alumnos ordenados por promedio ---")
    if asignatura is not None:
        print("Carrera:", asignatura["carrera"], "| Asignatura:", asignatura["asignatura"])

    print(
        "Matrícula".ljust(12)
        + "Apellido".ljust(15)
        + "Nombre".ljust(15)
        + "Promedio".ljust(10)
    )
    print("-" * 52)

    for i in range(1, len(lineas)):
        alumno = parsear_alumno(lineas[i])
        if alumno is not None:
            print(
                str(alumno["matricula"]).ljust(12)
                + alumno["apellido"].ljust(15)
                + alumno["nombre"].ljust(15)
                + str(round(promedio_alumno(alumno), 2)).ljust(10)
            )


def mostrar_menu():
    """Muestra el menú de opciones del programa."""
    print("\n--- Menú de opciones ---")
    print("1. Crear el archivo")
    print("2. Cargar registros de alumnos")
    print("3. Consultar registro de alumno")
    print("4. Mostrar listado de alumnos")
    print("5. Modificar registro de alumno")
    print("6. Borrar registro de alumno")
    print("7. Calcular promedios")
    print("8. Mayor y menor promedio")
    print("9. Aprobados y desaprobados")
    print("10. Ordenar por edad")
    print("11. Ordenar por promedio")
    print("12. Mostrar resultado (orden por promedio)")
    print("0. Salir")


# Programa principal
opcion = -1
while opcion != 0:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_archivo()
    elif opcion == 2:
        cargar_alumnos()
    elif opcion == 3:
        consultar_alumno()
    elif opcion == 4:
        mostrar_listado()
    elif opcion == 5:
        modificar_alumno()
    elif opcion == 6:
        borrar_alumno()
    elif opcion == 7:
        calcular_promedios()
    elif opcion == 8:
        mayor_menor_promedio()
    elif opcion == 9:
        generar_aprobados_desaprobados()
    elif opcion == 10:
        ordenar_por_edad()
    elif opcion == 11:
        ordenar_por_promedio()
    elif opcion == 12:
        mostrar_ordenados_por_promedio()
    elif opcion == 0:
        print("Fin del programa.")
    else:
        print("Opción inválida.")
