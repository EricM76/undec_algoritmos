# 📌 Consigna:
#
#  Crear un minijuego para tirar un dado y quitarle puntos de vida a un dragón.
# 1.Importar random.
# 2.Crear una variable vida_dragon = 60.
# 3.Crear la función tirarDado(lados) que reciba como argumento la cantidad de lados y devuelva un número aleatorio entre 1 y la cantidad de lados.
# 4.Crear la función atacarDragon() que sume el resultado de tirar un dado de 20 lados y uno de 4 lados, y retorne ese valor.
# 5.Restar el daño a vida_dragon.
# 6.Mostrar los puntos de vida restantes.

import random

vida_dragon = 60


# Devuelve un número aleatorio entre 1 y la cantidad de lados.
def tirarDado(lados):
    return random.randint(1, lados)


# El daño es la suma de un dado de 20 lados y uno de 4 lados.
def atacarDragon():
    dado_20 = tirarDado(20)
    dado_4 = tirarDado(4)
    dano = dado_20 + dado_4
    print(f"Dado de 20: {dado_20} | Dado de 4: {dado_4} | Daño total: {dano}")
    return dano


# Restar el daño a la vida del dragón y mostrar los puntos restantes.
dano = atacarDragon()
vida_dragon = vida_dragon - dano
print(f"Puntos de vida restantes del dragón: {vida_dragon}")
