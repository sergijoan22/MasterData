# Importamos librerias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos


# Cambiar el working directory, donde guarda las cosas
# Ponemos r delante para poner el string como raw
os.chdir(r'D:\Master\AnalisisDatos\Ejercicio_19nov_1')

# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Cargamos la tabla wbr usada en el ejercicio anterior
wbr = pd.read_csv('wbr_modificado.csv', sep = ',', decimal = ',')


# La columna con el uso de cada de dia (cnt_cat) 
# diviadio en tres grupos la pasamos a porcentajes
cnt_cat_columns = wbr.cnt_cat.value_counts()
n = cnt_cat_columns.sum()
cnt_cat_columns = (cnt_cat_columns / n) * 100
# Ahora tenemos en cnt_cat_columns el porcentaje de cada uso


# Ahora ya podemos mostrar cnt_cat al ver que el cambio ha salido bien
bar_list = cnt_cat_columns.index
plt.bar(bar_list, cnt_cat_columns)

# Estan las variables ordinales a parte de las cuanti y cuali
# Por ejemplo al medir algo como: Bueno, medio y malo.
# Se va a tratar el caso anterior como variables nominales
# Vemos la columna cnt_cat que esta guardado como string (object)
wbr.dtypes

# Importar para crear variables ordinales
from pandas.api.types import CategoricalDtype


# Primero definimos la lista de las categorias
my_categories = ['Uso bajo', 'Uso medio', 'Uso alto']
# Definimos el tipo de dato con la lista de categorias diciendole que están en orden
my_rentals_type = CategoricalDtype(categories = my_categories, ordered = True)
# Cremos una nueva columna que a partir de wbr_cat lo hacemos en tipo de dato ordinal
wbr['cnt_cat_ord'] = wbr.cnt_cat.astype(my_rentals_type)

# Ahora la nueva columna tiene que ser de tipo category
wbr.dtypes

# Guardamos un df con la cantidad de cada uso
cnt_cat_ord = pd.crosstab(index = wbr['cnt_cat_ord'], columns = 'count')

# Lo pasamos a porcentajes
n = cnt_cat_ord.sum()
cnt_cat_ord_porcien = (cnt_cat_ord / n) * 100

# Si ahora dibujamos la gráfica estará ordenado automáticamente
plt.bar(aa, cnt_cat_ord_porcien['count'])

















