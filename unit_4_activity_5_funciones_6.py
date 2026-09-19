# 📌 Consigna: 
#
# Desarrollar un programa que, por medio de funciones, permite validar la contraseña ingresada por un 
# usuario (la cual debe ser igual a ‘supersecreta_156’. Se deberán implementar las siguientes funciones en 
# la resolución: 
# - Función valida_intento(): controla si el usuario aún tiene intentos disponibles. Recibe como argumento la cantidad de intentos realizados hasta el momento y la cantidad máxima de intentos permitida y devuelve como valor de retorno una variable de tipo bandera (True o False) que indica si aún le quedan intentos o no. 
# - Función valida_pass(): determina si la contraseña es correcta o no. Recibe como argumento la contraseña y devuelve como valor de retorno una variable de tipo bandera (True o False) que indica si la contraseña es correcta o no. 
# 
# La cantidad máxima de intentos permitidos para la contraseña es de 3 (tres) y la comprobación realizada 
# en cada intento debe informarse con un mensaje en pantalla tal como ‘Contraseña correcta’ o ‘Contraseña 
# incorrecta’ según corresponda. Se sobreentiende que, si se ingresa la contraseña correcta, se debe informar
# y finalizar el programa sin completar los intentos faltantes.

PASSWORD_CORRECTA = "supersecreta_156"
MAX_INTENTOS = 3


# Recibe los intentos ya realizados y el máximo permitido.
# Devuelve True si todavía quedan intentos, False si se agotaron.
def valida_intento(intentos_realizados, max_intentos):
    return intentos_realizados < max_intentos


# Recibe la contraseña ingresada y devuelve True si coincide con la correcta.
def valida_pass(contrasena):
    return contrasena == PASSWORD_CORRECTA


intentos = 0
acceso = False

# Mientras queden intentos y no se haya acertado, se pide la contraseña
while valida_intento(intentos, MAX_INTENTOS) and not acceso:
    contrasena = input("Ingrese la contraseña: ")

    if valida_pass(contrasena):
        print("Contraseña correcta")
        acceso = True
    else:
        print("Contraseña incorrecta")
        intentos += 1
