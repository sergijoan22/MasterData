'''
Se pide que se introduzcan años hasta uno bisiesto.
'''

year = 7
bisiesto:bool = False

while bisiesto == False:
  ano = int(input("Introduce un año: "))
  if year % 4 == 0:
    bisiesto = True
print("Felicidades: El año es bisiesto")
