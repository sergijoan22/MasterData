'''
Recibimos un número de productos en temporada y un número de productos de fuera de temporada.
Aplicando un 30 % de descuento a los del segundo grupo, indicar la cantidad ahorrad
'''

precioProducto:float = 14.99

cantTemporada = int(input("Introduce los productos de temporada:"))
cantFueraTemporada = int(input("Introduce los productos de fuera de temporada:"))

precioTotal:float = (cantTemporada * precioProducto) + (cantFueraTemporada * 0.7 * precioProducto)
descuento:float = cantFueraTemporada * 0.3 * precioProducto

print(f"El precio total es de {precioTotal.__round__(2)} €")
print(f"El descuento es de {descuento.__round__(2)} €")
