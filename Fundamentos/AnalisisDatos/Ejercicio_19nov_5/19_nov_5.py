# Comparación de más de dos medias
# Vamos a comprarar los datos de ventas dependiendo de la condición meteorológica

# Importamos librerias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos
import scipy.stats as stats # Estadística
import seaborn as sns # Gráficos
from pandas.api.types import CategoricalDtype # Para variables ordinales

# Cambiar el working directory, donde guarda las cosas
# Ponemos r delante para poner el string como raw
os.chdir(r'D:\Master\AnalisisDatos\Ejercicio_19nov_5')
# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Ahora vamos a abrir otro cvs donde están todos los datos
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')

# Añadimos una columna con el tiempo en texto
wbr.loc[(wbr['weathersit'] == 1), 'weathersit_cat'] = 'Sunny'
wbr.loc[(wbr['weathersit'] == 2), 'weathersit_cat'] = 'Cloudy'
wbr.loc[(wbr['weathersit'] == 3), 'weathersit_cat'] = 'Rainy'

# Ver que se ha hecho bien
pd.crosstab(wbr.weathersit, wbr.weathersit_cat)

# Se debería convertir la variable a ordinal
# ya que hay un orden entre las condiciones
# así todos los gráficos saldrían ordenados

# Pasamos a ordinales las variables
# Primero definimos la lista de las categorias
my_categories = ['Sunny', 'Cloudy', 'Rainy']
# Definimos el tipo de dato con la lista de categorias diciendole que están en orden
wheater_type = CategoricalDtype(categories = my_categories, ordered = True)
# Creamos una nueva columna del tiempo pero con variables de tipo ordinal
wbr['weathersit_cat_ord'] = wbr.weathersit_cat.astype(wheater_type)

# Dibujamos que en porcentaje de dias hay cada tiempo
mytable = pd.crosstab(index = wbr["weathersit_cat_ord"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

# Agrupamos los datos de cnt por el tipo de tiempo
cnt_sunny = wbr.loc[wbr.weathersit_cat == 'Sunny', 'cnt']
cnt_cloudy = wbr.loc[wbr.weathersit_cat == 'Cloudy', 'cnt']
cnt_rainy = wbr.loc[wbr.weathersit_cat == 'Rainy', 'cnt']

# Hacemos un test anova para comprobar las medias
# Obtenemos uprimero el valor t
stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)[0]
# Obtenemos ahora el pvalue
stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)[1]
# El pvalue siendo menos que 0.05 nos hace rechazar la hipotesis nula
# de que todas las medias son iguales
# Hay por tanto diferencia de medias entre todas las medias
# o en una media con las otras

# Vemos la media de los 3 grupos
wbr.groupby('weathersit_cat_ord').cnt.mean()

# Vemos la media total y el total de casos para mostrar en el gráfico
wbr.cnt.mean()
wbr.cnt.count()

# Dibujamos las 3 medias en un gráfico
# Elegimos el tamaño del gráfico
plt.figure(figsize=(5,3))
# Creamos el gráfico
ax = sns.pointplot(x="weathersit_cat_ord", y="cnt", data=wbr,ci=99, join=0)
# Vamos a poner cuando poner los ticks del eje y y el rango de este
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(1000,6200)
# Ponemos una línea horizontal en la media total
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="blue")
# Vamos a añadir un cuadro con algunos datos
# ponemos la media total, el numero de datos, el pvalue y el valor de t que es otro dato de interés
props = dict(boxstyle = 'round', facecolor= 'white', lw=0.5)
# ponemos la media total, el numero de datos, el pvalue y el valor de t que es otro dato de interés
plt.text(2,3500,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
# Nombre del eje x
plt.xlabel('Weather type')
# Título del gráfico
plt.title('Average rentals by weather type.''\n')
plt.show()

plt.savefig('weather_means.svg')

'''
El intervalo de confianza de rainy es más grande porque hay menos datos
Aún así, el intervalo de confianza de rainy está fuera del de los otros
Por tanto, se puede deducir que la media de lod días rainy es diferente a los otros
Se podría confirmar haciendo un t test entre los datos de rainy y los de sunny o cloudy

Aparte, entre sunny y cloudy tampoco se solapan por lo que podemos asegurar que sus medias
son diferentes.

Todo esto lo podemos asegurar al 95%

Hemos puesto el el gráfico de confianza al 95, ahora se va a poner al 99% (ci = 99)
el mismo gráfico para ver si podemos estar seguros al 99%.

Seguimos viendo que los márgenes de los 3 grupos no se solapan por lo que
la media de los 3 grupos es diferente con seguridad del 99%
'''

# Ahora se va a hacer un box plot para visualizarlo de forma distinta
sns.boxplot(x = 'weathersit_cat_ord', y = 'cnt', data = wbr)

'''
En centro de la box es la mediana,
q1 y q3 son los bordes de la caja, que encierran del 25% al 75% de los datos
Los extremos o whiskers marca los límites a partir de los que no se esperan
datos. Si hay algún dato fuera de los whiskers es un outlier y se marca.

Sin embargo, con un box plot no podemos asegurar a ciertos niveles que las
medias son distintas
'''



