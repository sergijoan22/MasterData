'''
Se da una lista con diferentes productos y sus precios.
Ordenar los productos por precio.
'''

precios = [('Producto A', '12.20'), ('Producto B', '15.10'), ('Producto C', '24.50')]

#x representa cada uno de los elementos de la lista
print(sorted(precios, key = lambda x: float(x[1]), reverse = True))

# lambda x: es igual a ponder def myfunction(x):
