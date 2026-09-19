# 📌 Consigna:
#
# Una librería almacena en un archivo llamada libros.dat el siguiente registro de información sobre cada uno de 
# sus libros: 
#
# Registro: libro
#   entero: codigo
#   caracter: titulo
#   caracter: autor
#   caracter: genero
#   entero: ejemplaresVendidos
#   real: precio
# finRegistro
#
# Se solicita desarrollar un programa que permita manipular el archivo de libros por medio de un menú con las 
# siguientes opciones: 
# 1. Crear el archivo.
#   - Permite crear el archivo. En caso de que el archivo ya exista advertir con un mensaje en pantalla al 
#     usuario y solicitar que indique si desea crearlo nuevamente. 
# 2. Cargar registros de libros.
#   - Permite cargar registros de libros de manera ordenada. La condición para el fin de carga será un número 
#     de legajo igual a cero. 
# 3. Consultar registro de libro.
#   - Muestra la información de un libro. Para la búsqueda del libro se debe usar como campo clave el código. 
# 4. Mostrar listado de libros en formato tabla.
#   - Muestra el listado de todos los libros en formato tabla.
# 5. Modificar registro de libro.
#   - Permite modificar los campos correspondientes al género, precio y ejemplares vendidos. Para la búsqueda 
#     del libro a modificar usar como campo clave el código. 
# 6. Borrar registro de libro.
#   - Permite borrar un registro de un libro. Para la búsqueda del libro a eliminar usar como campo clave el número de legajo. 
#   - Luego de eliminar el libro deseado del archivo original se deberá copiar el mismo en otro archivo llamado librosBaja.dat. 
# 7. Calcular la recaudación total por libro.
#   - A partir del archivo libros.dat generar un archivo librosRecaudacion.dat que contenga información referida 
#     a la recaudación de cada libro. El registro a guardar en este archivo es el siguiente:

#   Registro: libroRecaudacion
#       entero: codigo
#       real: recaudacion
#   finRegistro
#
# 8. Informe de ejemplares vendidos por género del libro.
#   - Permite aplicar corte de control para generar un informe con los ejemplares vendidos por género donde 
#     se visualice la siguiente información:
#   Genero: <genero>
#   Código         Título         Ejemplares Vendidos
#   <codigo>       <titulo>       <ejemplaresVendidos>
#   ...
#   <codigo>       <titulo>       <ejemplaresVendidos>
#   Total: <totalEjemplaresVendidos>
#
# 9. Salir. 
#
#	Nota: implementar cada opción del menú por medio de funciones

import os

ARCHIVO_LIBROS = "libros.dat"
ARCHIVO_BAJA = "librosBaja.dat"
ARCHIVO_RECAUDACION = "librosRecaudacion.dat"


def parsear_libro(linea):
    """Convierte una línea del archivo en un diccionario de libro."""
    partes = linea.strip().split(" - ")
    if len(partes) != 6:
        return None
    return {
        "codigo": int(partes[0]),
        "titulo": partes[1],
        "autor": partes[2],
        "genero": partes[3],
        "ejemplaresVendidos": int(partes[4]),
        "precio": float(partes[5]),
    }


def formatear_libro(libro):
    """Convierte un diccionario de libro en una línea para el archivo."""
    return (
        str(libro["codigo"]) + " - "
        + libro["titulo"] + " - "
        + libro["autor"] + " - "
        + libro["genero"] + " - "
        + str(libro["ejemplaresVendidos"]) + " - "
        + str(libro["precio"]) + "\n"
    )


def leer_libros():
    """Lee todos los libros del archivo y los devuelve en una lista."""
    if not os.path.exists(ARCHIVO_LIBROS):
        return None

    archivo = open(ARCHIVO_LIBROS, "r")
    lineas = archivo.readlines()
    archivo.close()

    libros = []
    for linea in lineas:
        libro = parsear_libro(linea)
        if libro is not None:
            libros.append(libro)
    return libros


def guardar_libros(libros):
    """Guarda la lista de libros en el archivo, reemplazando el contenido."""
    archivo = open(ARCHIVO_LIBROS, "w")
    for libro in libros:
        archivo.write(formatear_libro(libro))
    archivo.close()


def archivo_existe_o_avisar():
    """Verifica si el archivo existe. Si no, avisa al usuario y retorna False."""
    if not os.path.exists(ARCHIVO_LIBROS):
        print("El archivo no existe. Primero debe crearlo (opción 1).")
        return False
    return True


def crear_archivo():
    """Crea el archivo de libros. Si ya existe, pregunta si se recrea."""
    if os.path.exists(ARCHIVO_LIBROS):
        print("El archivo ya existe.")
        respuesta = input("¿Desea crearlo nuevamente? (s/n): ").lower()
        if respuesta != "s":
            print("Operación cancelada.")
            return

    archivo = open(ARCHIVO_LIBROS, "w")
    archivo.close()
    print("Archivo creado correctamente.")


def cargar_libros():
    """Carga libros de forma ordenada por código. Finaliza con código 0."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()

    print("Carga de libros (código 0 para finalizar).")
    codigo = int(input("Ingrese código: "))

    while codigo != 0:
        existe = False
        for libro in libros:
            if libro["codigo"] == codigo:
                existe = True
                break

        if existe:
            print("Ya existe un libro con ese código.")
        else:
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            genero = input("Ingrese género: ")
            ejemplares = int(input("Ingrese ejemplares vendidos: "))
            precio = float(input("Ingrese precio: "))

            nuevo = {
                "codigo": codigo,
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "ejemplaresVendidos": ejemplares,
                "precio": precio,
            }

            insertado = False
            for i in range(len(libros)):
                if nuevo["codigo"] < libros[i]["codigo"]:
                    libros.insert(i, nuevo)
                    insertado = True
                    break
            if not insertado:
                libros.append(nuevo)

            print("Libro cargado correctamente.")

        codigo = int(input("Ingrese código: "))

    guardar_libros(libros)
    print("Carga finalizada.")


def consultar_libro():
    """Busca un libro por código y muestra sus datos."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()
    codigo = int(input("Ingrese el código a consultar: "))

    encontrado = False
    for libro in libros:
        if libro["codigo"] == codigo:
            print("\n--- Datos del libro ---")
            print("Código:", libro["codigo"])
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Género:", libro["genero"])
            print("Ejemplares vendidos:", libro["ejemplaresVendidos"])
            print("Precio:", libro["precio"])
            encontrado = True
            break

    if not encontrado:
        print("Libro no encontrado.")


def mostrar_listado():
    """Muestra todos los libros en formato tabla."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    print("\n--- Listado de libros ---")
    print(
        "Código".ljust(10)
        + "Título".ljust(20)
        + "Autor".ljust(18)
        + "Género".ljust(15)
        + "Ejemplares".ljust(12)
        + "Precio".ljust(10)
    )
    print("-" * 85)

    for libro in libros:
        print(
            str(libro["codigo"]).ljust(10)
            + libro["titulo"].ljust(20)
            + libro["autor"].ljust(18)
            + libro["genero"].ljust(15)
            + str(libro["ejemplaresVendidos"]).ljust(12)
            + str(libro["precio"]).ljust(10)
        )


def modificar_libro():
    """Modifica género, precio y ejemplares vendidos de un libro por código."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()
    codigo = int(input("Ingrese el código del libro a modificar: "))

    encontrado = False
    for libro in libros:
        if libro["codigo"] == codigo:
            print("Libro encontrado:", libro["titulo"])
            libro["genero"] = input("Ingrese nuevo género: ")
            libro["precio"] = float(input("Ingrese nuevo precio: "))
            libro["ejemplaresVendidos"] = int(input("Ingrese nuevos ejemplares vendidos: "))
            encontrado = True
            break

    if encontrado:
        guardar_libros(libros)
        print("Libro modificado correctamente.")
    else:
        print("Libro no encontrado.")


def borrar_libro():
    """Elimina un libro por código y lo copia en librosBaja.dat."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()
    codigo = int(input("Ingrese el código del libro a borrar: "))

    nuevos = []
    eliminado = None
    for libro in libros:
        if libro["codigo"] == codigo:
            eliminado = libro
        else:
            nuevos.append(libro)

    if eliminado is None:
        print("Libro no encontrado.")
        return

    archivo_baja = open(ARCHIVO_BAJA, "a")
    archivo_baja.write(formatear_libro(eliminado))
    archivo_baja.close()

    guardar_libros(nuevos)
    print("Libro borrado y copiado en", ARCHIVO_BAJA)


def calcular_recaudacion():
    """Genera librosRecaudacion.dat con código y recaudación de cada libro."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    archivo = open(ARCHIVO_RECAUDACION, "w")
    print("\n--- Recaudación por libro ---")
    print("Código".ljust(10) + "Recaudación".ljust(15))
    print("-" * 25)

    for libro in libros:
        recaudacion = libro["ejemplaresVendidos"] * libro["precio"]
        archivo.write(str(libro["codigo"]) + " - " + str(round(recaudacion, 2)) + "\n")
        print(str(libro["codigo"]).ljust(10) + str(round(recaudacion, 2)).ljust(15))

    archivo.close()
    print("Archivo", ARCHIVO_RECAUDACION, "generado correctamente.")


def informe_por_genero():
    """Aplica corte de control e informa ejemplares vendidos por género."""
    if not archivo_existe_o_avisar():
        return

    libros = leer_libros()

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    # Ordenar por género para aplicar corte de control
    ordenados = list(libros)
    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            if ordenados[j]["genero"] < ordenados[i]["genero"]:
                aux = ordenados[i]
                ordenados[i] = ordenados[j]
                ordenados[j] = aux

    print("\n--- Informe de ejemplares vendidos por género ---")

    i = 0
    while i < len(ordenados):
        genero_actual = ordenados[i]["genero"]
        total = 0

        print("\nGenero:", genero_actual)
        print("Código".ljust(12) + "Título".ljust(25) + "Ejemplares Vendidos")
        print("-" * 55)

        while i < len(ordenados) and ordenados[i]["genero"] == genero_actual:
            libro = ordenados[i]
            print(
                str(libro["codigo"]).ljust(12)
                + libro["titulo"].ljust(25)
                + str(libro["ejemplaresVendidos"])
            )
            total = total + libro["ejemplaresVendidos"]
            i = i + 1

        print("Total:", total)


def mostrar_menu():
    """Muestra el menú de opciones del programa."""
    print("\n--- Menú de opciones ---")
    print("1. Crear el archivo")
    print("2. Cargar registros de libros")
    print("3. Consultar registro de libro")
    print("4. Mostrar listado de libros")
    print("5. Modificar registro de libro")
    print("6. Borrar registro de libro")
    print("7. Calcular la recaudación total por libro")
    print("8. Informe de ejemplares vendidos por género")
    print("9. Salir")


# Programa principal
opcion = 0
while opcion != 9:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_archivo()
    elif opcion == 2:
        cargar_libros()
    elif opcion == 3:
        consultar_libro()
    elif opcion == 4:
        mostrar_listado()
    elif opcion == 5:
        modificar_libro()
    elif opcion == 6:
        borrar_libro()
    elif opcion == 7:
        calcular_recaudacion()
    elif opcion == 8:
        informe_por_genero()
    elif opcion == 9:
        print("Fin del programa.")
    else:
        print("Opción inválida.")
