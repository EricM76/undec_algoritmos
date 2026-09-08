# Queremos mostrar los números del 1 al 20.
# - Si un número es múltiplo de 3 y de 5, mostrar "¡Múltiplo de 3 y de 5!".
# - Si un número es múltiplo de 3, mostrar el mensaje "¡Múltiplo de 3!".
# - Si es múltiplo de 5, mostrar "¡Múltiplo de 5!".
# - Si no es múltiplo de ninguno, mostrar el número sin mensaje adicional.

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - ¡Múltiplo de 3 y de 5!")
    elif i % 3 == 0:
        print(f"{i} - ¡Múltiplo de 3!")
    elif i % 5 == 0:
        print(f"{i} - ¡Múltiplo de 5!")
    else:
        print(i)