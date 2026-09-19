# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su 
# símbolo o un mensaje de aviso si la divisa no está en el diccionario.
# 
# 📌 Pasos:
# 
# 1. Crear un diccionario para las divisas (divisas).
# 2. Cada diccionario debe tener las siguientes claves y valores:
#   - "Euro”:”€”
#   - "Dollar":”$”
#   - "Yen":”¥”
# 3. Solicitar al usuario una divisa.
# 4. Mostrar el símbolo asociado a la divisa o un mensaje de error.

# Crear un diccionario para las divisas.
divisas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}

# Solicitar al usuario una divisa.
divisa = input("Ingrese una divisa (Euro, Dollar o Yen): ")

# Mostrar el símbolo asociado a la divisa o un mensaje de error.
if divisa in divisas:
    print(f"El símbolo de {divisa} es: {divisas[divisa]}")
else:
    print("La divisa ingresada no está en el diccionario.")
