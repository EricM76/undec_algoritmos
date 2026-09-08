# 📌 Consigna:
# Importa el módulo time.
# - Muestra la hora actual en pantalla en formato H:M:S.
# - Espera 3 segundos.
# - Muestra el mensaje "¡Tiempo finalizado!".

import time

print(f"La hora actual es: {time.strftime('%H:%M:%S')}")
print("Espera 3 segundos...")
time.sleep(3)
print("¡Tiempo finalizado!")
