# Comparación de más de dos medias
# Vamos a comprarar los datos de ventas dependiendo de las estaciones

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
os.chdir(r'D:\Master\AnalisisDatos\Ejercicio_19nov_6')
# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Ahora vamos a abrir otro cvs donde están todos los datos
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')

# Añadimos una columna con el tiempo en texto
wbr.loc[(wbr['season'] == 1), 'season_cat'] = 'Winter'
wbr.loc[(wbr['season'] == 2), 'season_cat'] = 'Spring'
wbr.loc[(wbr['season'] == 3), 'season_cat'] = 'Summer'
wbr.loc[(wbr['season'] == 4), 'season_cat'] = 'Autumn'

# Ver que se ha hecho bien
pd.crosstab(wbr.season, wbr.season_cat)

# Se debería convertir la variable a ordinal
# ya que hay un orden entre las condiciones
# así todos los gráficos saldrían ordenados

# Pasamos a ordinales las variables
# Primero definimos la lista y orden de las categorias
my_categories = ['Spring', 'Summer', 'Autumn', 'Winter']
# Definimos el tipo de dato con la lista de categorias diciendole que están en orden
season_type = CategoricalDtype(categories = my_categories, ordered = True)
# Creamos una nueva columna del tiempo pero con variables de tipo ordinal
wbr['season_cat_ord'] = wbr.season_cat.astype(season_type)

# Dibujamos que en porcentaje de dias hay cada tiempo
mytable = pd.crosstab(index = wbr["season_cat_ord"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])
plt.show()

# Agrupamos los datos de cnt por el tipo de tiempo
cnt_spring = wbr.loc[wbr.season_cat_ord == 'Spring', 'cnt']
cnt_summer = wbr.loc[wbr.season_cat_ord == 'Summer', 'cnt']
cnt_autumn = wbr.loc[wbr.season_cat_ord == 'Autumn', 'cnt']
cnt_winter = wbr.loc[wbr.season_cat_ord == 'Winter', 'cnt']

# Hacemos un test anova para comprobar las medias
# Obtenemos uprimero el valor t
stats.f_oneway(cnt_spring, cnt_summer, cnt_autumn, cnt_winter)[0]
# Obtenemos ahora el pvalue
stats.f_oneway(cnt_spring, cnt_summer, cnt_autumn, cnt_winter)[1]
# El pvalue siendo menos que 0.05 nos hace rechazar la hipotesis nula
# de que todas las medias son iguales
# Hay por tanto diferencia de medias entre todas las medias
# o en una media con las otras

# Vemos la media de todas las estaciones
wbr.groupby('season_cat_ord').cnt.mean()

# Vemos la media total y el total de casos para mostrar en el gráfico
wbr.cnt.mean()
wbr.cnt.count()

# Dibujamos las 3 medias en un gráfico
# Elegimos el tamaño del gráfico
plt.figure(figsize=(5,3))
# Creamos el gráfico
ax = sns.pointplot(x="season_cat_ord", y="cnt", data=wbr,ci=99, join=0)
# Vamos a poner cuando poner los ticks del eje y y el rango de este
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(1000,6200)
# Ponemos una línea horizontal en la media total
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="blue")
# Vamos a añadir un cuadro con algunos datos
# ponemos la media total, el numero de datos, el pvalue y el valor de t que es otro dato de interés
props = dict(boxstyle = 'round', facecolor= 'white', lw=0.5)
plt.text(2.4,4500,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
# Nombre del eje x
plt.xlabel('Weather type')
# Título del gráfico
plt.title('Average rentals by season.''\n')
plt.show()
