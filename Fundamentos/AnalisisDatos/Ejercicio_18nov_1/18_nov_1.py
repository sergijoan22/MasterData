# Importamos librerias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos


# Directorio de trabajo
os.chdir(r'D:\Master\AnalisisDatos\Ejercicios\18_nov_1')
# Lo comprobamos
os.getcwd()


# Cargar dataset
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')

# Vemos dimensiones del dataframe
wbr.shape

# Vemos las ultimas filas
wbr.tail()

# Vemos en un histograma las ventas (cnt)
plt.hist(wbr.cnt)

# SUBSETTING
# Guardamos las variables que nos interesan
my_vars = ['temp_celsius', 'cnt']
# Creamos un dataframe con las variables que nos interesan
wbr_minimal = wbr[my_vars]


# Ahora vamos a seleccionar casos
# wbr tiene datos de 2011 y 2012
# Vamos a coger los de 2011 solo

#Primero vemos que años hay en el df
mytable = wbr.groupby(['yr']).size()
mytable

#Podemos verlo en porcentajes
n = mytable.sum()
mytable2 = (mytable / n) * 100
mytable2

# 0 es 2011 y 1 es 2012
# Nos quedamos con los del 2011
wbr_2011 = wbr[wbr.yr == 0]
# Lo mostramos
plt.hist(wbr_2011.cnt)
# Vemos la estadistica
wbr_2011.cnt.describe

# Ahora solo del invierno de 2012
# En los datos, en la columna season, invierno es el 1
wbr_2012_winter = wbr[(wbr.yr == 1) & (wbr.season == 1)]
# Vemos la forma
wbr_2012_winter.shape
# Lo mostramos
plt.hist(wbr_2012_winter.cnt, edgecolor = 'black')

# Ahora de invierno y otoño de cualquier año
# En los datos, en la columna season, invierno es el 4
wbr_autumn_winter = wbr[(wbr.season == 1) | (wbr.season == 4)]
# Vemos la forma
wbr_autumn_winter.shape
# Lo mostramos
plt.hist(wbr_autumn_winter.cnt, edgecolor = 'black')


# Limpiamos el entorno con reset -f
# Cargamos un nuevo df
wbr_ue = pd.read_csv('wbr_ue.csv', sep = ';', decimal = ',')

# Vemos los datos de la temperatura del df
wbr_ue.temp_celsius.describe()
# Nos sale un valor máximo de 99, lo cual es un error
# Por ello, primero dibujar los datos para poder detectarlo
plt.hist(wbr_ue.temp_celsius)
# Podemos sacar los registros con los datos de temp erroneos
wbr_eu_errores = wbr_ue[wbr_ue.temp_celsius > 70]
# Estos tienen un 99 en temperatura
# En algunos datasets, se poden numeros como 99, -1..
# para detallar cierto caso especial

# Un outlier es un data muy alejado de lo normal
# pero que no es un dato erróneo

# Creamos una columna con la temperatura
# pero cambiando los 99 por un None (nan)
wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99, np.nan)

# Ahora ya sacamos la media de temp con los errores quitados
wbr_ue.temp_celsius_c.describe()
# Y graficamente
plt.hist(wbr_ue.temp_celsius_c)
# Puede dar error si hay algun nan
# Para ello, podemos extraer lon nan de la columna
wbr_ue.temp_celsius_c.dropna()
# Y haciendo el histograma sobre ello
plt.hist(wbr_ue.temp_celsius_c.dropna())

# Tambien se puede quitar los casos donde haya algun nan en al menos una columna
# No es recomendable, ya que el nan puede estar en columnas no usadas
# Si se puede usar en un df con las columnas elegidas para usarlas
# Ahora se crea un df sin ni un nan
wbr_ue2 = wbr_ue.dropna()


# TRANSFORMAR DATOS

# Hacemos un reset

# Cargamos el archivo con los datos
# wbr_eu era un dataset sucio para hacer pruebas, wbr esta limpio
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')


# Tenemos una columna con usuarios registrados y otra que no, registered y casual
# Creamos una columna con el ratio entre ambos
wbr['cs_ratio'] = wbr.casual / wbr.registered

# analizamos la columna creada
wbr.cs_ratio.describe()

# Borramos la columna cnt, que es la suma de registered y casual
del wbr['cnt']
# Se puede volver a crear facilmente
wbr['cnt'] = wbr.casual + wbr.registered

# RECODING
# Tenemos en la columna season: 1 invierno, 2 primavera...
# Podemos cambiarlo a la manera que prefiramos
# Vamos a crear una columna con datos en str poniendo los nombres de las estaciones
# en loc ponemos las coordenadas de donde queremos hacer los cambios, en que filas y columna
# Ponemos en la columna Invierno en las filas que season es 1 y asi para cada estacion
wbr.loc[(wbr['season'] == 1), 'season_cat'] = 'Winter'
wbr.loc[(wbr['season'] == 2), 'season_cat'] = 'Spring'
wbr.loc[(wbr['season'] == 3), 'season_cat'] = 'Summer'
wbr.loc[(wbr['season'] == 4), 'season_cat'] = 'Autumn'
# Si hubiese alguna fila no definida en la nueva columna, se pondria un nan
# Para comprobar que se ha hecho bien, se hace una tabla cruzada de la variable original y la cruzada
pd.crosstab(wbr.season, wbr.season_cat)

# Ahora vamos a cambiar una columna cuantitativa en una nominal
# Agrupar los valores por rangos en varias categorias
# Vamos a hacerlo de la columna cnt, con los usos de las bicis cada dia
# Vamos a hacer 3 grupos, dentro de (media - std) y (media + std), por abajo y por arriba
# Analizamos los datos para elegir como agrupar los registros
res = wbr['cnt'].describe()
# Guardamos la media y la std
media = res[1]
std = res[2]
lower_limit = media - std
upper_limit = media + std

# Ahora creamos la nueva columna con los datos de cnt agrupados
wbr.loc[(wbr['cnt'] <= lower_limit), 'cnt_cat'] = 'Uso bajo'
wbr.loc[(wbr['cnt'] > lower_limit) & (wbr['cnt'] < upper_limit), 'cnt_cat'] = 'Uso medio'
wbr.loc[(wbr['cnt'] >= upper_limit), 'cnt_cat'] = 'Uso alto'
# Ahora comprobamos que se ha hecho bien con una tabla cruzada
pd.crosstab(wbr.cnt, wbr.cnt_cat)
# Al haber tantos valores distintos en cnt, la tabla cruzada no sirve mucho
# Mejor hacer un scatter plot para comprobar
plt.scatter(wbr.cnt, wbr.cnt_cat)
# Vemos entonces en y los valores de cnt_cat y que valores de x (cnt) ha cogido
plt.plot(wbr.dteday, wbr.cnt)
# Ahora ya podemos mostrar cnt_cat al ver que el cambio ha salido bien
plt.hist(wbr.cnt_cat, width = 0.5)








