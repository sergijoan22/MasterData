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
os.chdir(r'D:\Master\AnalisisDatos\Tarea2')
# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

##############################################################################

# Ahora vamos a abrir otro cvs donde están todos los datos
# Leemos las columnas de interés
colum_leer = ['Nationality', 'Height']
df = pd.read_csv('players_fifa22.csv', usecols = colum_leer)

# Cambiamos el nombre de la columna Height
df.rename(columns={'Height': 'Altura'}, inplace=True)

# Añadimos una columna llamada Nacionalidad con las nacionalidades de los jugadores en español
df.loc[df['Nationality'] == 'Netherlands', 'Nacionalidad'] = 'Países bajos'
df.loc[df['Nationality'] == 'Denmark', 'Nacionalidad'] = 'Dinamarca'
df.loc[df['Nationality'] == 'Spain', 'Nacionalidad'] = 'España'
df.loc[df['Nationality'] == 'Mexico', 'Nacionalidad'] = 'México'
df.loc[df['Nationality'] == 'India', 'Nacionalidad'] = 'India'

# Ver que se ha hecho bien
pd.crosstab(df.Nationality, df.Nacionalidad)

# Eliminamos los jugadores que no son de estas nacionalidades
df.dropna(subset = ['Nacionalidad'], inplace = True)


# Pasamos a ordinales la variable Nacionalidad
# Primero definimos la lista y orden de las categorias
# Se usa el orden de altura promedio de los datos generales
categorias_Nacionalidad = ['Países bajos', 'Dinamarca', 'España', 'México', 'India']
# Definimos el tipo de dato con la lista de categorias diciendole que están en orden
tipo_Nacionalidad = CategoricalDtype(categories = categorias_Nacionalidad, ordered = True)
# Creamos una nueva columna del tiempo pero con variables de tipo ordinal
df['Nacionalidad_ord'] = df.Nacionalidad.astype(tipo_Nacionalidad)


# Dibujamos que en porcentaje de dias hay cada tiempo
n_paises = pd.crosstab(index = df["Nacionalidad_ord"], columns="count")
n=n_paises.sum()[0]
n_paises_100 = (n_paises / n)*100
plt.bar(n_paises_100.index, n_paises_100['count'])
plt.show()

# Entre estos dato destaca que cerca de la mitad de los datos son de España
# Lo que significa que tiene muchos más jugadores en el juego que los otros países


# Agrupamos los datos de altura por la nacionalidad del jugador
Altura_pai = df.loc[df.Nacionalidad_ord == 'Países bajos', 'Altura']
Altura_din = df.loc[df.Nacionalidad_ord == 'Dinamarca', 'Altura']
Altura_esp = df.loc[df.Nacionalidad_ord == 'España', 'Altura']
Altura_mex = df.loc[df.Nacionalidad_ord == 'México', 'Altura']
Altura_ind = df.loc[df.Nacionalidad_ord == 'India', 'Altura']


# Hacemos un test anova para comprobar las medias
# Obtenemos el tvalue y el pvalue
t, p = stats.f_oneway(Altura_pai, Altura_din, Altura_esp, Altura_mex, Altura_ind)
p
# El pvalue siendo menos que 0.05 nos hace rechazar la hipotesis nula
# de que todas las medias son iguales
# Hay por tanto diferencia de medias entre todas las medias
# o en una media con las otras


# Vemos la media de altura de los países
df.groupby('Nacionalidad_ord').Altura.mean()



# Dibujamos las 3 medias junto a sus intervalos de confianza en un gráfico
# Elegimos el tamaño del gráfico
plt.figure(figsize=(5,4))
# Creamos el gráfico
ax = sns.pointplot(x="Nacionalidad_ord", y="Altura", data=df,ci=95, join=0)


# Vamos a poner cuando poner los ticks del eje y y el rango de este
plt.yticks(np.arange(174, 186, step=2))
plt.ylim(174, 186)

# Ponemos una línea horizontal en la media total
plt.axhline(y=df.Altura.mean(), linewidth=1, linestyle= 'dashed', color="blue")

# Vamos a añadir un cuadro con algunos datos
# ponemos la media total, el numero de datos, el pvalue y el valor de t que es otro dato de interés
props = dict(boxstyle = 'round', facecolor= 'white', lw=0.5)
media = str(df.Altura.mean().__round__(1))
n = str(n)
t = format(t, '.3f')
p = format(p, '.3f')
texto_caja = 'Mean: ' + media + '\nn: ' + n + '\nt: ' + t + '\np value: ' + p
plt.text(3, 182.5, texto_caja, bbox=props)

# Nombre del eje x
plt.xlabel('Nacionalidad')
# Título del gráfico
plt.title('Promedio de altura por Nacionalidad\nen los jugadores de FIFA 22')
plt.show()











