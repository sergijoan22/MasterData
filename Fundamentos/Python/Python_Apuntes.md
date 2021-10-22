# Python

## Imprimir texto por pantalla

```python
print("Hola mundo")
nombre = "Sergi"
print(nombre + " Sastre")
print(f"{nombre} Sastre")
saludo = f"{nombre} Sastre"
print(saludo)
```

## Tipar variables

Tipar variables para que no puedan cambiar de tipo

```python
apellido:str="Sastre"
edad:int=23
apellido:float = 1.80
hombre:bool=True
```

## Lista

Conjunto de elementos. Se puede específicar que sean de un único tipo.

```python
miLista: [str] = ['Martín', 'Alberto', 'Sofía'] 
miListaDeDatosCombinados = [42, 3.14, 'hola', 25, False,(1, 2), {1:"uno", 2:"dos"}]

print(miLista)
print(*miLista)
print(miLista[2])
```

## Diccionario

Lista de elementos donde cada uno tiene un identificador.

```python


miDiccionario = dict()
persona = {
  "nombre": "Sergi",
  "apellido": "Sastre",
  "edad": 22,
}
print(*persona)
print(f'La edad de {persona["nombre"]} es {persona["edad"]}')
print(f'La edad de {persona.get("nombre")} es {persona.get("edad")}')
```

## Tupla

Lista de elementos que no se puede modificar.

```python
miTupla = (5, "Hola mundo!", True, -4.5)
```

## Set

Conjunto de datos sin orden que no se repite.

```python
miSetDeNumeros = set([1, 2, 3, 3, 5, 1, 5])
print(*miSetDeNumeros)

miOtroSetDeDatos = {1, 2, 3, 5, 5, 'a', False}
print(miOtroSetDeDatos)
```

Se puede congelar un set para que no se pueda modificar luego.

```python
miSetCongelado = frozenset(misNumeros)
print(*miSetCongelado)
```



## Constantes

No hay forma de declarar una constante, por lo que se hace igual que una variable pero poniendo el nombre en mayúsculas para identificarlas.

```python
NUMERO_PI = 3.141516
```

## Cadenas

```python
miCadena:str = "hola mundo"
miCadena2:str = 'QUe pasa mundo'
miCadena_primera_palabra = miCadena[0:4]
print(f'La primera palabra de la variable miCadena es {miCadena_primera_palabra}')
print(f'La primera palabra de la variable miCadena es {miCadena[0:4]}')
print(f'La variable miCadena en mayúsculas es {miCadena.upper()}')
print(f'La variable miCadena capitalizado es {miCadena.capitalize()}')
```

## Rangos

Para crear un conjunto de números sobre los que iterar.

```python
#Este va desde el 1 al 9 de 2 en 2
miRango = range(1, 10, 2)
print(*miRango)

#Este va desde 10 a 2, de 1 en 1 pero hacia abajo
miRango2 = range(10, 1, -1)
print(*miRango2)
```

## Sentencias y bucles

```python
for i in range(11):
  if i % 2 == 0:
    print(i)
print('\n')

lista = [4, 3, 3, 4, 6, 3, 4, 5, 4]
while len(lista) > 3:
  lista.pop()
  print(*lista)
```

## Crear una función

```python
def funcionSuma (a, b):
  print(f"¡{a+b}!")

funcionSuma(3,5)
funcionSuma("Hola","Mundo")
```

```python
#Si no sabemos cuantos parámetros vamos a recibir
def miFuncionConMultiplesParametros(*elementos) :
    for elemento in elementos:
        print(f"Elemento: {elemento}")
        
lista: [int] = [4, 5, 3, 9, 6, 7]
miFuncionConMultiplesParametros(*lista, 6, 4, 5)
#Ponemos antes * para especificar que no queremos pasar la lista, si no sus valores
```

## Fechas

Se necesitan las siguientes librerías

```python
import datetime
import time
```

```python
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
```

```python
ahora = datetime.datetime.now()
timeStamp = time.mktime(ahora.timetuple())
print('TimeStamp', timeStamp)

print('Fecha legible', datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S'))
miFecha = '13/06/1954'
nuevoTimeStamp = time.mktime(datetime.datetime.strptime(miFecha,'%d/%m/%Y').timetuple())

print(nuevoTimeStamp)
print('Fecha nueva legible', datetime.datetime.fromtimestamp(nuevoTimeStamp).strftime('%Y-%m-%d'))


```

