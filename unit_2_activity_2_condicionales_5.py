# 📌 Consigna:
# Generar un algoritmo para una empresa que paga a sus vendedores un sueldo bruto igual a la suma de un sueldo básico de $550.000 más una comisión que es igual a un porcentaje del monto total vendido. El porcentaje por comisión depende de la categoría del vendedor de acuerdo a la siguiente tabla:
# - SENIOR: Más de 6 años de experiencia, 14.25%
# - SEMI-SENIOR: Entre 2 y 6 años de experiencia, 13.00%
# - JUNIOR: Menos de 2 años de experiencia, 11.75%
# Por otro lado, si el sueldo bruto del vendedor es mayor a $300.000, se efectúa un descuento igual al 15% del sueldo bruto; en caso contrario, se efectúa un descuento igual al 10% del sueldo bruto.
# Diseñe un algoritmo que determine el sueldo básico, la comisión, el sueldo bruto, el descuento y el sueldo neto de un vendedor de la empresa.

# Parte fija del sueldo (no depende de las ventas ni de la categoría)
input_sueldo_basico = 150000
input_experiencia = int(input("Ingrese la experiencia del vendedor: "))
input_monto_vendido = int(input("Ingrese el monto total vendido: "))

# El % de comisión depende de los años: el if/elif entra en el PRIMERO que cumpla
# > 6 → SENIOR 14.25% | 2 a 6 → SEMI-SENIOR 13% | menos de 2 → JUNIOR 11.75%
if input_experiencia > 6:
    input_comision = input_monto_vendido * 0.1425
elif input_experiencia >= 2:
    input_comision = input_monto_vendido * 0.13
else:
    input_comision = input_monto_vendido * 0.1175

# Bruto = lo fijo + lo que ganó por vender
input_sueldo_bruto = input_sueldo_basico + input_comision

# El descuento se calcula SOBRE el bruto: más de 300000 → 15%; si no → 10%
if input_sueldo_bruto > 300000:
    input_descuento = input_sueldo_bruto * 0.15
else:
    input_descuento = input_sueldo_bruto * 0.10

# Neto = lo que realmente cobra (bruto menos descuento)
input_sueldo_neto = input_sueldo_bruto - input_descuento

print(f"El sueldo básico es: {input_sueldo_basico}")
print(f"La comisión es: {input_comision}")
print(f"El sueldo bruto es: {input_sueldo_bruto}")
print(f"El descuento es: {input_descuento}")
print(f"El sueldo neto es: {input_sueldo_neto}")