# 📌 Consigna:
# Desarrollar un programa que permita cargar tres números enteros y por medio de funciones determine lo siguiente:
# - Función menor(): determina el menor de los tres números ingresados. Recibe como argumento los tres números
#   ingresados y devuelve el menor.
# - Función mayor(): determina el mayor de los tres números ingresados. Recibe como argumento los tres números
#   ingresados y devuelve el mayor.
# - Función signo():permite determinar si los tres números ingresados fueron todos del mismo signo, es decir,
#   todos positivos o todos negativos, o si hay valores positivos y negativos mezclados en la serie ingresada.
#   Recibe como argumento los 3 números ingresados y devuelve una bandera que indica uno de los dos estados
#   posibles. -
# - Función compartenSigno(): es invocada sólo cuando todos los números ingresados fueron todos del mismo
#   signo y permite generar la suma de los números multiplicada por el mayor encontrado anteriormente


# Recibe los tres números y devuelve el menor de ellos.
def menor(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


# Recibe los tres números y devuelve el mayor de ellos.
def mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Recibe los tres números y devuelve True si todos tienen el mismo signo
# (todos positivos o todos negativos). Devuelve False si hay signos mezclados.
# El 0 no es positivo ni negativo, por lo que no comparte signo con el resto.
def signo(a, b, c):
    todos_positivos = a > 0 and b > 0 and c > 0
    todos_negativos = a < 0 and b < 0 and c < 0
    return todos_positivos or todos_negativos


# Solo se invoca cuando los tres números tienen el mismo signo.
# Devuelve la suma de los tres números multiplicada por el mayor ya calculado.
def compartenSigno(a, b, c, el_mayor):
    return (a + b + c) * el_mayor


n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
n3 = int(input("Ingrese el tercer número entero: "))

el_menor = menor(n1, n2, n3)
el_mayor = mayor(n1, n2, n3)
mismo_signo = signo(n1, n2, n3)

print(f"El menor es: {el_menor}")
print(f"El mayor es: {el_mayor}")

if mismo_signo:
    print("Los tres números tienen el mismo signo.")
    resultado = compartenSigno(n1, n2, n3, el_mayor)
    print(f"La suma de los números multiplicada por el mayor es: {resultado}")
else:
    print("Los números tienen signos mezclados.")
