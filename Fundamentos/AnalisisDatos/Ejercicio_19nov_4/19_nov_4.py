# Hacer un test para ver si hay diferencia entre las ventas de 2011 y 2012

# Importamos librerias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos
import scipy.stats as stats # Estadística
import seaborn as sns # Gráficos

# Cambiar el working directory, donde guarda las cosas
# Ponemos r delante para poner el string como raw
os.chdir(r'D:\Master\AnalisisDatos\Ejercicio_19nov_4')
# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Ahora vamos a abrir otro cvs donde están todos los datos
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')

# Añadimos una columna con workingday en números
wbr.loc[(wbr['yr'] == 0), 'yr_numero'] = '2011'
wbr.loc[(wbr['yr'] == 1), 'yr_numero'] = '2012'

# Ver que se ha hecho bien la nueva columna
pd.crosstab(wbr.yr, wbr.yr_numero)

# Vemos los datos dependiendo del año
wbr.groupby('yr_numero').cnt.describe()
wbr.groupby('yr_numero').cnt.mean()

# Sacamos datos de ventas para cada año
cnt_wd = wbr.loc[wbr.yr_numero == 2011, 'cnt']
cnt_nwd = wbr.loc[wbr.yr_numero == 2012, 'cnt']

# Hacemos un ttest con las ventas de ambos años y sacamos el t y pvalue
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)

# Sacamos el total y la media de todos los datos para el gráfico
wbr.cnt.mean()
wbr.cnt.count()

# Hacemos la gráfica con las dos medias
ax = sns.pointplot(x = 'yr_numero', y = 'cnt', data = wbr, ci = 95, join = 0)
# Vamos a añadir una línea horizontal en la media total
plt.axhline(y = wbr.cnt.mean(),
               linewidth = 1,
               linestyle = 'dashed',
               color = 'blue',)
# Vamos a poner cuando poner los ticks del eje y y el rango de este
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
# Vamos a añadir un cuadro con algunos datos
# ponemos la media total, el numero de datos, el pvalue y el valor de t que es otro dato de interés
props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
plt.text(-0.2, 5400, 'Mean: 4504.3''\n''n:731' '\n' 't: -15.578' '\n' 'Pval.:0.000', bbox=props)
# Añadimos nombre al eje x
plt.xlabel('Year')
#Añadimos título al gráfico
plt.title('Average rentals per year.''\n')

'''
Estamos 99.999 convencidos que el año la media de alquileres de bicis
de los dos años fue diferente en Washington
'''



