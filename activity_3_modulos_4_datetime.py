# 📌 Consigna:
# Importa el módulo time.
# - Muestra la hora actual en pantalla en formato H:M:S.
# - Espera 3 segundos.
# - Muestra el mensaje "¡Tiempo finalizado!".

import time  # módulo para medir, formatear y pausar el tiempo

# strftime arma un texto con la hora del sistema
# %H = hora (00-23), %M = minutos, %S = segundos  →  "14:05:09"
print(f"La hora actual es: {time.strftime('%H:%M:%S')}")

print("Espera 3 segundos...")
# sleep(n) frena el programa n segundos; el siguiente print no corre hasta que termine
time.sleep(3)
print("¡Tiempo finalizado!")
