'''
Partiendo de:
- cantidad a invertir
- el interés anual
- El número de años

Calcular el capital obtenido, guardarlo en una variable y mostrarlo en consola

"El capital obtenido por tu inversión asciende a "capital_obtenido" € (dos decimales)"
'''

cantidadInvertir:float = 20000
numeroAnos:float = 5
interesAnual:float = 2

capitalObtenido:float = cantidadInvertir * (1 + numeroAnos * interesAnual)
print(f"El capital obtenido por tu inversión asciende a {capitalObtenido.__round__(2)} €") 
