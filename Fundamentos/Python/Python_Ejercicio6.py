'''
Preguntar la Edad.
Devolver si eres menor de edad, jubilado o en edad de trabajar.
'''

miEdad:int = int(input("Edad: "))

if miEdad > 65:
  print("Eres jubilado")
elif miEdad < 18:
  print("Eres menor de edad")
else:
  print("Edad de trabajar")
