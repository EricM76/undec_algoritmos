# 📌 Consigna:
# Generar un programa para una tienda que vende productos a precios unitarios los cuales dependen de un código asignado a los mismos:

# Código 1 a 25 -> Precio Unitario: $ 277,7
# Código 26 a 50 -> Precio Unitario: $ 255,5
# Código 51 a 75 -> Precio Unitario: $ 230,5
# Código 76 en adelante -> Precio Unitario: $ 210,5

# Adicionalmente, si el cliente adquiere más de 50 unidades la tienda le descuenta el 15% del importe de la compra;  en caso contrario, sólo le descuenta el 5%.
# Se solicita diseñar un algoritmo que permita ingresar el código de un producto junto con la cantidad vendida y determine:
# - el importe de la compra, 
# - el importe del descuento y 
# - el importe a pagar por la compra.

input_codigo = int(input("Ingrese el código del producto: "))
input_cantidad = int(input("Ingrese la cantidad vendida: "))

if input_codigo >= 1 and input_codigo <= 25:
    input_precio_unitario = 277.7
elif input_codigo >= 26 and input_codigo <= 50:
    input_precio_unitario = 255.5
elif input_codigo >= 51 and input_codigo <= 75:
    input_precio_unitario = 230.5
elif input_codigo >= 76:
    input_precio_unitario = 210.5
else:
    input_precio_unitario = 0

if input_precio_unitario == 0:
    print("El código del producto es incorrecto")
else:
    input_importe_compra = input_precio_unitario * input_cantidad

    if input_cantidad > 50:
        input_descuento = input_importe_compra * 0.15
    else:
        input_descuento = input_importe_compra * 0.05

    input_importe_pagar = input_importe_compra - input_descuento

    print(f"El importe de la compra es: {input_importe_compra}")
    print(f"El importe del descuento es: {input_descuento}")
    print(f"El importe a pagar es: {input_importe_pagar}")