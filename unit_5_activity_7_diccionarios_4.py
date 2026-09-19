# Queremos guardar la información de un superhéroe en un diccionario.
# 📌 Pasos:
# 1. Crear una variable llamada superheroe y asignarle un diccionario vacío.
# 2. Agregar seis propiedades utilizando la siguiente sintaxis:
#    superheroe["clave"] = valor
# 3. Las claves pueden ser: "nombre", "edad", "ciudad", "origen", "alias", "universo", etc.
# 
# DESAFIO:
# ¿Podes lograr que el superhéroe tenga más de un poder, pero todos almacenados en una sola clave llamada "poderes"?

# Crear una variable llamada superheroe y asignarle un diccionario vacío.
superheroe = {}

# Agregar seis propiedades utilizando la notación de corchetes.
superheroe["nombre"] = "Peter Parker"
superheroe["edad"] = 18
superheroe["ciudad"] = "Nueva York"
superheroe["origen"] = "Estados Unidos"
superheroe["alias"] = "Spider-Man"
superheroe["universo"] = "Marvel"

# DESAFÍO: guardar más de un poder en una sola clave llamada "poderes".
superheroe["poderes"] = ["sentido arácnido", "trepar paredes", "super fuerza"]

# Mostrar el diccionario por consola para verificar su contenido.
print(superheroe)
