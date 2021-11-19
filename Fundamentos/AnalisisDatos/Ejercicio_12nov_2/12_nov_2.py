# Importamos las librerias a usar
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos

# Cambiar el working directory
# Ponemos r delante para poner el string como raw
os.chdir(r'C:\Users\sergi\OneDrive\Máster\Fundamentos\Introduccion_analisis_datos\Proyectos\12_nov_2')

# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Abrimos un csv y lo guardamos en un dataframe
# Especificamos que en el csv el separador es el punto y coma
# Especificamos que en el csv los decimales se definen por coma
rentals_2011 = pd.read_csv('washington_bike_rentals_2011.csv', sep = ';', decimal = ',')

# Del dataframe
# Mostrar dimensionalidad
rentals_2011.shape
# Mostrar 3 primeras lineas
rentals_2011.head(3)
# Mostrar laas dos ultimas lineas
rentals_2011.tail(2)

# Sobre las columnas del df:
# season = invierno, primavera...
# weekday = 0/domingo, 1/lunes...
# holiday = si son vacaciones
# workinkday = si es laborable
# casual = Usuarios casuales, no registrados
# registered = usuarios registrados
# cnt = suma de ambos tipos de usuarios

# De la columna con los usuarios de cada dia sacamos la media
np.mean(rentals_2011.cnt)
# Nos devuelve un float pero lo redondeamos
np.mean(rentals_2011.cnt).__int__()

# De la columna con los usuarios de cada dia sacamos la standard desviation
np.std(rentals_2011.cnt)

# Aunque la mejor forma de hacer la media
rentals_2011.cnt.mean()
# Y redondeado
rentals_2011.cnt.mean().__int__()

# Y la mejor para la standard desviation
rentals_2011.cnt.std().__int__()

# Y directamente, para obtener de una varios datos
rentals_2011.cnt.describe()

'''
count    total de valores
mean     media
std      desviación típica
min      valor mínimo
25%      primer cuartil
50%      segundo cuartil o mediana
75%      tercer cusartil
max      valor máximo
'''

# Ahora dibujamos un histograma
plt.hist(rentals_2011.cnt)

# Vamos a hacer otra versión del histograma
# Primero, guardamos la columna de cnt en una variable
x = rentals_2011['cnt']
# O se puede hacer también como
x = rentals_2011.cnt
# La segunda no funciona si en el nombre de la columna hay espacios o otros carácteres especiales
# Ahora hacemos el histograma poniendo bordes a las barras
plt.hist(x, edgecolor = 'black')


# Vamos a añadir cosas  (Correr el las instrucciones de la grafica a la vez)
# Con bins hacemos las barras más extrechas
plt.hist(x, edgecolor = 'black', bins = 20)
# Añadimos puntes de corte de la gráfica. De 0 a 7000 de 1000 en 1000
plt.xticks(np.arange(0, 7000, step = 1000))
# Añadimos un título
plt.title('Figure 1. Frecuencua del total de usos de bicicletas')
# Etiqueta en el eje y
plt.ylabel('Frecuencia')
# Etiqueta en el eje x
plt.xlabel('Número de usos')
# Con la siguiente función cerramos el gráfico
# Las siguientes instrucciones ya no modifican el gráfico actual si no a uno nuevo
# Además muestra solo el gráfico sin más cosas
plt.show()


# Es importante el dataset con información adicional
# Por ejemplo, añadir que tiempo hacía durante el año

# Guardamos el csv con esos datos en un df
weather_2011 = pd.read_csv('weather_washington_2011.csv', sep = ';', decimal = ',')

# Mostrar dimensionalidad
weather_2011.shape
# Mostrar 3 primeras lineas
weather_2011.head(3)
# Mostrar laas dos ultimas lineas
weather_2011.tail(2)
# Para saber los tipos de datos del df
weather_2011.dtypes
# QC OK (mensaje para confirmarnos que el df está bien)


# Borramos la vairable x que no vamos a usar de momento
del(x)

# Ahora vamos a hacer un merge de los dos df
# Hay que tener en cuenta que esten ordenados igual
# Necesitamos en cada df un id único que esté en ambos
# Por ejemplo, podemos usar la columna day o dteday
# És recomendable usar uno que sea númerico, así que usaremos day
rentals_weather_2011 = pd.merge(rentals_2011, weather_2011, on = 'day')

# Mostrar dimensionalidad
rentals_weather_2011.shape
# De las columnas que tienen el mismo nombre en ambas, se guardan las dos
# Para la columna que usamos el merge, solo se guarda una ya que se supone que són iguales
# Mostrar 3 primeras lineas
rentals_weather_2011.head(3)
# Mostrar laas dos ultimas lineas
rentals_weather_2011.tail(2)
# Para saber los tipos de datos del df
rentals_weather_2011.dtypes

# Como tenemos dteday que está repetida en el nuevo df quitamos una
del rentals_weather_2011['dteday_x']
# A la que queda le cambiamos el nombre 
rentals_weather_2011 = rentals_weather_2011.rename(columns = {'dteday_y': 'dteday'})

# Ahora podemos borrar los otros dos df, ya que los hemos juntado
del(rentals_2011)
del(weather_2011)

# A la hora de cargar o guardar una tabla, añadimos: ignore_index = True
# Para que no carge o lea la columna con de índice

# Tenemos un csv con los mimos datos pero de 2012, que queremos añadir a nuestro df
# En este caso se añadiria por abajo creando nuevas filas
# Cargamos el csv
rentals_weather_2012 = pd.read_csv('rentals_weather_2012.csv', sep = ';', decimal = ',')

# Mostrar dimensionalidad
rentals_weather_2012.shape
# Vemos que este tiene 366 filas, cuando hay 365 días. Es porque 2012 es bisiesto
# Mostrar 3 primeras lineas
rentals_weather_2012.head(3)
# Mostrar laas dos ultimas lineas
rentals_weather_2012.tail(2)
# QC OK (mensaje para confirmarnos que el df está bien)

# Creamos un df con los datos de 2011 y de 2012
# ignore_index para 
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index = True)

# Borramos los df de 11 y de 12 que ya no vamos a usar
del(rentals_weather_2011)
del(rentals_weather_2012)

# Guardamos el df en una variable para manejarlo mejor
wbr = rentals_weather_11_12

# Vamos a analizar la columna wheather
# Rompemos el df en grupos dependiendo de la columna weathersit y nos dice el tamaño de cada
mytable = wbr.groupby(['weathersit']).size()

# Ahora podemos ver que valores son mas comunes
mytable

# Vemos el total de valores
total = mytable.sum()
# Mejor este método que ver el tamaño del df ya que puede haber datos vacíos

# Con ambos datos, podemos sacar los porcentajes de cada uno
mytable2 = (mytable / total) * 100
mytable2

# Ahora estos datos los queremos redondear
mytable3 = round(mytable2, 1)
mytable3

# Ahora con estos datos vamos a representar con una gráfica
# Debemos específicar las etiquetas que le vamos a poner a las barras
bar_list = ['Sunny', 'Cloudy', 'Rainy']
# Ya la podemos dibujar
plt.bar(bar_list, mytable2, edgecolor = 'black')
# Etiqueta del eje y
plt.ylabel('Percentage')
# Añadimos un título a la gráfica
plt.title('Figure 1. Percentage of weather situations')
# Escribir en las coordenadas 1.7 y 50 el total de casos
plt.text(1.7, 50, 'n: 731')

# Exportamos el gráfico en formato eps, para usarlo en programas de edición
# Permite editar los elementos del gráfico
plt.savefig('bar1.eps')
# Ahora en un formato jpg
# El problema es que es una calidad pobre, al hacer zoom, etc.
plt.savefig('bar1.jpg')
# Ahora en un formato svg que mantiene la calidad ya que no es una imagen fija
# Al hacer zoom redibuja las líneas, etc.
# El problema es que es menos compatible
# Si se va a usar luego un pdf, usar un svg mejor
plt.savefig('bar1.svg')


# Ahora vamos a abrir otro cvs donde están todos los datos
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')

# Obtenemos los datos de interés
wbr.cnt.describe()
# La desviación típica es el promedio de variaciones de cada valor respecto a la media

# Ahora vamos a dibujar
x = wbr['cnt']
plt.hist(x, edgecolor = 'black')
ticks = np.arrange(0, 10000, 1000)
plt.xticks(ticks)

# Guardamos la media y std para luego mostrarlos en la gráfica
res = wbr.cnt.describe()
# En esta series, los índices tienen los nombres
# Se puede acceder con estos índices
media = res['mean']
sd = res['std']
n = res['count']


























































































