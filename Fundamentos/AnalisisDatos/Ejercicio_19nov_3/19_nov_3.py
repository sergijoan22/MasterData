# Importamos librerias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos


# Cambiar el working directory, donde guarda las cosas
# Ponemos r delante para poner el string como raw
os.chdir(r'D:\Master\AnalisisDatos\Ejercicio_19_nov_3')

# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Ahora vamos a abrir otro cvs donde están todos los datos
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ';', decimal = ',')

# Vamos a ver si la media de alquileres en los días de trabajo es mayor a los de fiesta
# Numéricamente podemos hacer un t test
# Gráficamente un gráfico de intervalos de confianza

# Vemos la característica de cnt
wbr.cnt.describe()
plt.hist(wbr.cnt)

# Añadimos una columna con workingday en números
wbr.loc[(wbr['workingday'] == 0), 'workingday_cat'] = 'Free day'
wbr.loc[(wbr['workingday'] == 1), 'workingday_cat'] = 'Working day'

# Ver que se ha hecho bien
pd.crosstab(wbr.workingday, wbr.workingday_cat)

# Dibujamos que porcentaje de dias son wd y cuales no
mytable = pd.crosstab(index=wbr["workingday_cat"],
columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])



# Vemos datos dependiendo de si es festivo o no
wbr.groupby('workingday_cat').cnt.describe()
wbr.groupby('workingday_cat').cnt.mean()

# Ahora vamos como extrapolar los datos a toda la población
# Sacamos datos de ventas de wd y de no wd
cnt_wd = wbr.loc[wbr.workingday == 1, 'cnt']
cnt_nwd = wbr.loc[wbr.workingday == 0, 'cnt']


# Importamos una librería para hacer estadística
import scipy.stats as stats

# Vamos a hacer un t test comparando las dos medias eliginedo ser conservador
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
# Nos da un pvalue de 0.11, que lo podemos obtener directamente
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)[1]

'''
p value es la probabilidad que no haya ninguna diferencia
entre los dos grupos
El estándar suele estar aceptar a partir de un 0.05 hacia abajo
Al tener más, no tenemos evidencia suficientepara decir que 
la media de ventas entre los dias de trabajo y los que no es diferente

Vamos a dibujar la media de ambos casos, añadiendo un 95% de margen de confianza
Para el 95% la media estará en el intervalo dibujado
Cuando estos dibujos no se solapan en el eje y, se puede afirmar que si hay diferencia

Para hacer un gráfico para dibujar las medias, necesitamos una librería
import seaborn as sns
'''

# Hacemos la gráfica con las dos medias
# ci es el margen de confianza que añademos a cada punto
# join = 0 para no hacer una linea entre los puntos
ax = sns.pointplot(x = 'workingday_cat', y = 'cnt', data = wbr, ci = 95, join = 0)
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
plt.text(0.85, 5400, 'Mean: 4504.3''\n''n:731' '\n' 't: 1.601' '\n' 'Pval.:0.110', bbox=props)
# Añadimos nombre al eje x
plt.xlabel('Working Day')
#Añadimos título al gráfico
plt.title('Average rentals by Working Day.''\n')






































