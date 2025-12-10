# Crear una tienda de ropa
# Precio de la ropa

precio_camiseta = 10
precio_sudaderas = 20.5
precio_gorra = 5.5
iva = 0.21

# Introducir cantidad de artículo
cantidad_camisetas = int(input("Introduce cantidad de camisetas: "))
cantidad_sudaderas = int(input("Introduce cantidad de sudaderas: "))
cantidad_gorras = int(input("Introduce cantidad de gorras: "))

# Calcular total de precios
total_suma = (precio_camiseta * cantidad_camisetas + precio_sudaderas * cantidad_sudaderas + precio_gorra * cantidad_gorras)

# Precio total con IVA
precio_total = total_suma * (1 + iva)

# Mostrar el total de la compra
print("\nResumen de la compra:")
print("Subtotal:", total_suma, "euros")
print("Total con IVA:", precio_total, "euros")

