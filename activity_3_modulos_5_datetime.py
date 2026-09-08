# 📌 Consigna:
# Importar el módulo datetime.
# Crear una variable llamada ahora que guarde la fecha actual con datetime.datetime.now().
# - Hacer un print() de la fecha actual.
# Crear una variable llamada fecha, que guarde tu fecha de nacimiento con datetime.datetime(AÑO, MES, DÍA).
# - Hacer un print() de la fecha de nacimiento.
# Crear una variable llamada diferencia, que guarde la resta entre ahora y fecha.
# - Hacer un print() del resultado.
# Crear una variable llamada diferenciaEnDias que guarde solo los días de la diferencia (diferencia.days).
# - Hacer un print() del resultado.
# Crear una variable anios que guarde la edad en años dividiendo diferenciaEnDias entre 365.
# - Convertir el resultado a entero con int().
# - Hacer un print() del resultado.
# Mostrar un mensaje con el resultado en pantalla:
# - Tengo ___ años
# 💡 Ejemplo de salida esperada:
# - Fecha actual: 2025-03-18 10:30:45
# - Fecha de nacimiento: 1998-06-15 00:00:00
# - Diferencia en días: 9735
# - Tengo 26 años

import datetime  # módulo de la biblioteca estándar para fechas y horas

# now() toma la fecha y hora del sistema en este momento
ahora = datetime.datetime.now()
print(f"Fecha actual: {ahora}")

# datetime(año, mes, día) arma una fecha concreta (la hora queda en 00:00:00)
fecha = datetime.datetime(1990, 1, 1)
print(f"Fecha de nacimiento: {fecha}")

# Restar dos datetime da un timedelta: días + horas + minutos + segundos
diferencia = ahora - fecha
print(f"Diferencia: {diferencia}")

# .days se queda solo con la parte entera de días (descarta horas y minutos)
diferenciaEnDias = diferencia.days
print(f"Diferencia en días: {diferenciaEnDias}")

# Dividimos por 365 para pasar de días a años e int() recorta los decimales
# (es una edad aproximada: no contempla años bisiestos)
anios = int(diferenciaEnDias / 365)
print(f"Tengo {anios} años")

# Alternativa: misma lógica, pero la fecha de nacimiento la carga el usuario

ahora = datetime.datetime.now()
print(f"Fecha actual: {ahora}")

# Pedimos las tres partes por separado y las convertimos a entero
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de nacimiento: "))
dia_nacimiento = int(input("Ingrese el día de nacimiento: "))

# Armamos el datetime con los valores ingresados
fecha = datetime.datetime(anio_nacimiento, mes_nacimiento, dia_nacimiento)
print(f"Fecha de nacimiento: {fecha}")

diferencia = ahora - fecha
print(f"Diferencia: {diferencia}")

diferenciaEnDias = diferencia.days
print(f"Diferencia en días: {diferenciaEnDias}")

anios = int(diferenciaEnDias / 365)
print(f"Tengo {anios} años")