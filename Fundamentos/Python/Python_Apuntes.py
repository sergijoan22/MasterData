
print("Hola mundo")
nombre = "Sergi"
print(nombre + " Sastre")
# Otra forma de hacerlo
print(f"{nombre} Sastre")
# Otra forma de hacerlo, guardando todo en una variable
saludo = f"{nombre} Sastre"
print(saludo)

#Tipar variables
apellido:str="Sastre"
edad:int=23
apellido:float = 1.80
hombre:bool=True
#Si las tipamos ya no pueden cambiar de tipo
print('\n')

#Diccionario	
miDiccionario = dict()
 
miDiccionario = {
    "nombre": "Martin",
    "apellidos": "San José",
    "edad": 28,
    "email": "masajo@edem.es"
}

print(miDiccionario)

#Tupla (como lista pero no se puede modificar)
miTupla = (5, "Hola mundo!", True, -4.5)

#Lista
#Se puede especificar que sean de un único tipo
miListaDeContactos: [str] = ['Martín', 'Alberto', 'Sofía'] 
miListaDeDatosCombinados = [42, 3.14, 'hola', 25, False,(1, 2), {1:"uno", 2:"dos"}]

#Las constantes se suele y debe definir en mayúsculas
NUMERO_PI = 3.141516

miCadena:str = "hola mundo"
miCadena2:str = 'QUe pasa mundo'
miCadena_primera_palabra = miCadena[0:4]
print(f'La primera palabra de la variable miCadena es {miCadena_primera_palabra}')
print(f'La primera palabra de la variable miCadena es {miCadena[0:4]}')
print(f'La variable miCadena en mayúsculas es {miCadena.upper()}')
print(f'La variable miCadena capitalizado es {miCadena.capitalize()}')
print('\n')

miLista:[str] = ['Martín', 'Juan', 'Ana']
print(miLista)
#Para mostrar la lista mejor
print(*miLista)
#Mostrar un elemento
print(miLista[2])
print('\n')

#Rangos
#Este va desde el 1 al 9 de 2 en 2
miRango = range(1, 10, 2)
print(miRango)
print(*miRango)
#Este va desde 10 a 2, de 1 en 1 pero hacia abajo
miRango2 = range(10, 1, -1)
print(*miRango2)
print('\n')

persona = {
  "nombre": "Sergi",
  "apellido": "Sastre",
  "edad": 22,
}
print(persona)
print(*persona)
print(f'La edad de {persona["nombre"]} es {persona["edad"]}')
print(f'La edad de {persona.get("nombre")} es {persona.get("edad")}')
print('\n')

#SET: Datos que no se repiten y que se ordenan sin orden alguno
misNumeros = [1, 2, 3, 3, 5, 1, 5]
print(*misNumeros)
miSetDeNumeros = set(misNumeros)
print(*miSetDeNumeros)
miOtroSetDeDatos = {1, 2, 3, 5, 5, 'a', False}
print(miOtroSetDeDatos)
#Se puede congelar un set, lo que hace que no se pueda modificar luego
miSetCongelado = frozenset(misNumeros)
print(*miSetCongelado)
print('\n')

#NONE: Para instanciar una variable que no le queremos dar valor

#[_T] se refiere a algo genérico, que puede tener cualquier tipo de dato

#TODO: Operación aritmética que realice ((6-2)/5)^2
resultadoOperacion:float = ((6-2)/5)**2
print(round(resultadoOperacion, 4))
#De la siguiente manera se hace lo mismo, pero con otra sintaxis
print(resultadoOperacion.__round__(4))


'''
La consola le pide al usuario los datos de una peli:
  Nombre(str)
  Año (int)
  puntuación (float entre 1 y 5)
  director (str)
  género (comedia, drama, terror, acción). Las opciones se guardan en una lista para comprobar si se introduce una respuesta válida.
Se guarda en un diccionario llamado película favorita
'''

c:int = 4
d:int = 3
print(c == d)
print(c is not d)
print('\n')

#La variable i se crea globalmente, se puede usar luego
for i in range(11):
  if i % 2 == 0:
    print(i)
print('\n')

lista = [4, 3, 3, 4, 6, 3, 4, 5, 4]

while len(lista) > 3:
  lista.pop()
  print(*lista)

#Crear una función
def funcionSuma (a, b):
  print(f"¡{a+b}!")

funcionSuma(3,5)
funcionSuma("Hola","Mundo")

#Si no sabemos cuantos parámetros vamos a recibir 
def miFuncionConMultiplesParametros(*elementos) :
    for elemento in elementos:
        print(f"Elemento: {elemento}")
 
# llamando la función y pasándole una lista de parámetros
lista: [int] = [4, 5, 3, 9, 6, 7]
miFuncionConMultiplesParametros(*lista, 6, 4, 5)
#Ponemos antes * para especificar que no queremos pasar la lista, si no sus valores

#Paso por referencia o valor. Por defecto la primera, cambia el contenido de una variable al llamarla. Al hacerlo por valor, modifica una copia no el original.

#Fechas
#Necesitamos importar librerías
import datetime
import time
#Permite obtener eventos de un calendario
import calendar
#Locale permite escoger el idioma
import locale

#Ponemos el idioma en español
##locale.setlocale(locale.LC_ALL, 'es_ES')

print("Fecha y hora actual: ", datetime.datetime.now())
print("Año actual: ", datetime.date.today())
print("Año actual: ", datetime.date.today().strftime("%y"))
print("Año actual: ", datetime.date.today().strftime("%Y"))
print("Año actual: ", datetime.date.today().strftime("%B"))
print("Mes actual: ", datetime.date.today().strftime("%m"))
print("Número de la semana: ", datetime.date.today().strftime("%w"))
print("Día del año: ", datetime.date.today().strftime("%j"))
print("Día del mes: ", datetime.date.today().strftime("%d"))
print("Día de la semana: ", datetime.date.today().strftime("%A"))
print('Primer día de la semana: ', calendar.day_name[0])
print('Mes: ', calendar.month_name[10])
print('2020 es bisiesto: ', calendar.isleap(2020))

ahora = datetime.datetime.now()
#Cojemos la fecha de ahora 
timeStamp = time.mktime(ahora.timetuple())
print('TimeStamp', timeStamp)

print('Fecha legible', datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S'))
miFecha = '13/06/1954'
nuevoTimeStamp = time.mktime(datetime.datetime.strptime(miFecha,'%d/%m/%Y').timetuple())

print(nuevoTimeStamp)
print('Fecha nueva legible', datetime.datetime.fromtimestamp(nuevoTimeStamp).strftime('%Y-%m-%d'))


