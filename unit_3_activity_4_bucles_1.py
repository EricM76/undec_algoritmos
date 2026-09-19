# 📌 Consigna:
# Queremos mostrar los números del 1 al 20.
# - Si un número es múltiplo de 3 y de 5, mostrar "¡Múltiplo de 3 y de 5!".
# - Si un número es múltiplo de 3, mostrar el mensaje "¡Múltiplo de 3!".
# - Si es múltiplo de 5, mostrar "¡Múltiplo de 5!".
# - Si no es múltiplo de ninguno, mostrar el número sin mensaje adicional.

# Recorremos del 1 al 20 (range(1, 21): el 21 no se incluye)
for i in range(1, 21):
    # % (MOD) da el resto: si el resto es 0, i es múltiplo de ese número
    # Este if va PRIMERO: 15 es múltiplo de 3 Y de 5.
    # Si preguntáramos solo por 3 antes, 15 caería ahí y nunca veríamos el mensaje combinado
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - ¡Múltiplo de 3 y de 5!")
    elif i % 3 == 0:
        print(f"{i} - ¡Múltiplo de 3!")
    elif i % 5 == 0:
        print(f"{i} - ¡Múltiplo de 5!")
    else:
        # No es múltiplo de 3 ni de 5: solo se muestra el número
        print(i)