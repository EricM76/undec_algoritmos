# 📌 Consigna:
# Se solicita generar un programa que permita ingresar el día actual de la semana en una variable de tipo string (str); y otro día de la semana cualquiera en otra variable string (str) y luego realice las siguientes acciones:
# - Determinar el tamaño o longitud de cada día de la semana ingresado y mostrarlos.
# - Determinar si alguno de los días ingresados tiene más de 5 caracteres o 5 caracteres para luego mostrar mensajes tales como “El día DOMINGO tiene más de 5 caracteres”; “El día LUNES tiene 5 caracteres”.
# - Determinar si el primer día ingresado es igual a “LUNES” y mostrar un mensaje tal como “Comienzo de la semana laboral”. 
# - Determinar si el segundo día ingresado es igual a “SÁBADO” y mostrar un mensaje tal como “Comienzo del fin de semana”.
# - Ordenar alfabéticamente los días de la semana ingresados y mostrarlos ordenados.
# - Concatenar ambos días de la semana y mostrarlos en pantalla.
# - Repetir tres veces cada día de la semana y mostrarlos (Tener en cuenta que esta operación solo se puede realizar en Python)
# Nota: normalizar las cadenas de caracteres correspondientes a días de la semana antes de usarlos dentro de una condición.

input_dia_actual = input("Ingrese el día actual de la semana: ").strip().upper()
input_dia_semana = input("Ingrese otro día de la semana: ").strip().upper()
input_dia_actual = input_dia_actual.replace("SABADO", "SÁBADO").replace("MIERCOLES", "MIÉRCOLES")
input_dia_semana = input_dia_semana.replace("SABADO", "SÁBADO").replace("MIERCOLES", "MIÉRCOLES")

print(f"El tamaño o longitud del día {input_dia_actual} es: {len(input_dia_actual)}")
print(f"El tamaño o longitud del día {input_dia_semana} es: {len(input_dia_semana)}")

if len(input_dia_actual) > 5:
    print(f"El día {input_dia_actual} tiene más de 5 caracteres")
elif len(input_dia_actual) == 5:
    print(f"El día {input_dia_actual} tiene 5 caracteres")

if len(input_dia_semana) > 5:
    print(f"El día {input_dia_semana} tiene más de 5 caracteres")
elif len(input_dia_semana) == 5:
    print(f"El día {input_dia_semana} tiene 5 caracteres")

if input_dia_actual == "LUNES":
    print("Comienzo de la semana laboral")

if input_dia_semana == "SÁBADO":
    print("Comienzo del fin de semana")

if input_dia_actual < input_dia_semana:
    print(f"Los días ordenados alfabéticamente son: {input_dia_actual}, {input_dia_semana}")
else:
    print(f"Los días ordenados alfabéticamente son: {input_dia_semana}, {input_dia_actual}")

print(f"Los días concatenados son: {input_dia_actual + input_dia_semana}")
print(f"El día {input_dia_actual} repetido tres veces es: {input_dia_actual * 3}")
print(f"El día {input_dia_semana} repetido tres veces es: {input_dia_semana * 3}")