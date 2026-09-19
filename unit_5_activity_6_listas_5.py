# 📌 Consigna:
#
# Tenemos una lista con los puntajes más altos de un juego de arcade. Vamos a editar los valores y a agregar nuevos.
# puntajes = [1000, 950, 920, 830, 750]
#
# Pasos:
# 1. Crear una variable con una lista vacía.
# 2. Agregar a la lista los siguientes puntajes (de mayor a menor) utilizando el método correspondiente:
#   a. 1000
#   b. 950
#   c. 920
#   d. 830
#   e. 750
# 3. Quitar de la lista los siguientes puntajes utilizando el método correspondiente:
#   a. 920
#   b. 830
#   c. 750
# 4. Crear una variable llamada contador y asignarle el valor 0. Esta variable servirá como contador.
# 5. Solicitar al usuario la cantidad de puntajes que desea agregar utilizando input().
#    Guardar el valor ingresado en una variable llamada cantidadPuntajes.
# 6. Crear un bucle while para verificar que el valor ingresado en cantidadPuntajes sea un número.
#    Si no lo es, volver a pedir el valor.
#    Si lo es, convertirlo a entero y continuar.
# 7. Crear otro bucle while para que se ejecute mientras contador sea menor que cantidadPuntajes.
# 8. Dentro del segundo while:
#    a. Aumentar la variable contador en 1.
#    b. Crear una variable puntaje con un input() para pedir al usuario el puntaje a ingresar.
#    c. Mostrar el mensaje:
#       Ingresá el puntaje #1:
#       Ingresá el puntaje #2:
#       ... etc.
#    d. Usar el método necesario para agregar ese puntaje a la lista.
# 9. Al finalizar, mostrar por consola el mensaje:
#    Los 3 mejores puntajes son: ________
#    Mostrando los 3 mejores puntajes

# 1. Crear una variable con una lista vacía.
puntajes = []

# 2. Agregar los puntajes de mayor a menor.
puntajes.append(1000)
puntajes.append(950)
puntajes.append(920)
puntajes.append(830)
puntajes.append(750)

# 3. Quitar los puntajes indicados.
puntajes.remove(920)
puntajes.remove(830)
puntajes.remove(750)

# 4. Crear una variable llamada contador y asignarle el valor 0.
contador = 0

# 5. Solicitar la cantidad de puntajes a agregar.
cantidadPuntajes = input("Ingrese la cantidad de puntajes que desea agregar: ")

# 6. Verificar que el valor ingresado sea un número.
while not cantidadPuntajes.isdigit():
    cantidadPuntajes = input("Valor inválido. Ingrese un número: ")

cantidadPuntajes = int(cantidadPuntajes)

# 7 y 8. Pedir cada puntaje mientras el contador sea menor que la cantidad.
while contador < cantidadPuntajes:
    contador = contador + 1
    puntaje = input(f"Ingresá el puntaje #{contador}: ")

    while not puntaje.isdigit():
        puntaje = input(f"Valor inválido. Ingresá el puntaje #{contador}: ")

    puntajes.append(int(puntaje))

# 9. Mostrar los 3 mejores puntajes.
puntajes.sort(reverse=True)
print(f"Los 3 mejores puntajes son: {puntajes[:3]}")
