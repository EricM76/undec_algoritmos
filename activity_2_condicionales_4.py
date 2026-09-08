# 📌 Consigna:
# Generar un algoritmo para cargar por teclado las notas obtenidas por un estudiante en tres parciales rendidos durante el cursado de una asignatura universitaria (si no hizo el parcial deberá cargarse 0).
# Además, se carga la nota final que ese estudiante obtuvo en el desarrollo de los trabajos prácticos en esa misma asignatura.
# Se sabe que al terminar el cursado de la materia, todo alumno puede quedar en uno de los siguientes estados académicos:
# - Libre: si no llegó a cumplir con las condiciones para ser Regular.
# - Regular: todos los parciales rendidos, al menos dos de los tres parciales con nota de 4 (cuatro) o más y además obtuvo nota de 4 (cuatro) o más en la nota final de trabajos prácticos.
# - Promocionado: si aprobó los tres parciales con nota de 7 (siete) o más pero con promedio entre ellos de 9 (nueve) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
# - Aprobado: si aprobó los tres parciales con nota de 7 (siete) o más pero con promedio entre ellos de 8 (ocho) o más, y además obtuvo nota de 8 (ocho) o más en la nota final del práctico.
# El programa debe determinar y mostrar por pantalla el estado en que finalmente quedó el estudiante.

input_notas = [
    int(input("Ingrese la nota del primer parcial: ")), 
    int(input("Ingrese la nota del segundo parcial: ")), 
    int(input("Ingrese la nota del tercer parcial: ")), 
    int(input("Ingrese la nota final: "))]

promedio_parciales = (input_notas[0] + input_notas[1] + input_notas[2]) / 3
todos_parciales_rendidos = input_notas[0] != 0 and input_notas[1] != 0 and input_notas[2] != 0
al_menos_dos_con_cuatro = (
    (input_notas[0] >= 4 and input_notas[1] >= 4)
    or (input_notas[0] >= 4 and input_notas[2] >= 4)
    or (input_notas[1] >= 4 and input_notas[2] >= 4)
)

if input_notas[0] >= 7 and input_notas[1] >= 7 and input_notas[2] >= 7 and promedio_parciales >= 9 and input_notas[3] >= 8:
    print("Promocionado")
elif input_notas[0] >= 7 and input_notas[1] >= 7 and input_notas[2] >= 7 and promedio_parciales >= 8 and input_notas[3] >= 8:
    print("Aprobado")
elif todos_parciales_rendidos and al_menos_dos_con_cuatro and input_notas[3] >= 4:
    print("Regular")
else:
    print("Libre")