def calcular_precio_total(precio_producto, cantidad, descuento, iva):
    # Precio sin descuento ni iva
    subtotal = precio_producto * cantidad

    #Precio con descuento
    subtotal_con_descuento = precio_descuento(subtotal, descuento)

    #Precio con IVA
    precio_total = iva_aplicado(subtotal_con_descuento, iva)
   
    return precio_total


# Precio con descuento
def precio_descuento(subtotal, descuento):
    descuento_aplicado = subtotal * (descuento / 100)
    return subtotal - descuento_aplicado

# Aplicar IVA
def iva_aplicado(subtotal, iva):
    iva_aplicado = subtotal * (iva / 100)
    return subtotal + iva_aplicado

# Pedir al usuario los datos
nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduce el precio por unidad del producto: "))
cantidad = int(input("Introduce la cantidad de productos que deseas comprar: "))
descuento = float(input("Introduce el descuento en porcentaje: "))
iva = float(input("Introduce el IVA en porcentaje: "))

# Calcular el precio total llamando a la función
precio_total = calcular_precio_total(precio_producto, cantidad, descuento, iva)

# Mostrar el resultado
print(f"\nEl precio total del producto '{nombre_producto}' es: {precio_total} euros")


