'''
Se pida al usuario un año. Devolver si es o no bisiesto
'''

year = int(input("Introduce un año: "))

if year % 4 == 0:
  print("El año es bisiesto")
else:
  print("El año no es bisiesto")
