# Importamos las librerías necesarias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos

# Cambiar el working directory, donde guarda las cosas
os.chdir(r'D:\Master\AnalisisDatos\Tareas\Tarea1')

# Comprobamos que se ha cambiado el directorio
os.getcwd()

# Leemos ambos csv
df_expectancy = pd.read_csv('LifeExpectanceCountriesYears.csv', sep = ',', decimal = '.')
df_regiones = pd.read_csv('Regions.csv', sep = ',', decimal = '.')

# Cambiamos de los nombres de columnas los espacios por guiones bajo
#df_expectancy.columns = df_expectancy.columns.str.replace(' ', '_')
#df_regiones.columns = df_regiones.columns.str.replace(' ', '_')

# Creamos un dataframe con todos los datos
df_total = pd.merge(df_expectancy, df_regiones, on = 'Country Code')


# ANALIZAMOS EL DF
# Vemos la forma
df_total.shape
# Vemos los primeros registros
df_total.head(5)
# Vemos los últimos registros
df_total.tail(5)
# Para saber los tipos de datos del df
df_total.dtypes
# QC OK (mensaje para confirmarnos que el df está bien)

# Vemos todas las regiones
regiones = df_total['Region'].unique()

#WE OBTAIN DF FOR EACH REGION
# df for eurasia and oceania
regions_eao = ['South Asia', 'Europe & Central Asia', 'East Asia & Pacific']
df_EuAsOc = df_total.loc[df_total.Region.isin(regions_eao)]

# df for america
regions_a = ['Latin America & Caribbean', 'North America']
df_America = df_total.loc[df_total.Region.isin(regions_a)]

# df for africa and middle east
regions_ame = ['Sub-Saharan Africa', 'Middle East & North Africa']
df_AfMe = df_total.loc[df_total.Region.isin(regions_ame)]

# OBTAIN SERIES WITH LIFE EXPECTANCIES FOR EACH REGION
EuAsOc_life_exp = df_EuAsOc['2019']
America_life_exp = df_America['2019']
AfMe_life_exp = df_AfMe['2019']

# We remove empty values, countries which do not have data
EuAsOc_life_exp = EuAsOc_life_exp.dropna()
America_life_exp = America_life_exp.dropna()
AfMe_life_exp = AfMe_life_exp.dropna()

# ANALIZAMOS LOS DATOS PARA CADA SERIE
EuAsOc_life_exp.describe()
America_life_exp.describe()
AfMe_life_exp.describe()


# HISTOGRAMA CON LOS DATOS DE EUROPA, ASIA Y OCEANÍA
# Creamos el histograma
plt.hist(EuAsOc_life_exp, edgecolor = 'black', color = '#568AE4', bins = 15)
# Añadimos un título
plt.title('Figura 1. Frecuencia de la esperanza de vida\nen Europa, Asia y Oceanía en 2019')
# Añadimos nombre a los ejes
plt.ylabel('Frecuencia')
plt.xlabel('Esperanza de vida')
# Guardamos el gráfico en formato svg
plt.savefig('hist_EuAsOc.svg')
# Terminamos con el gráfico
plt.show()

# HISTOGRAMA CON LOS DE ÁMERICA
# Creamos el histograma
plt.hist(America_life_exp, edgecolor = 'black', color = '#568AE4', bins = 15)
# Añadimos un título
plt.title('Figura 2. Frecuencia de la esperanza de vida\nen Ámerica en 2019')
# Añadimos nombre a los ejes
plt.ylabel('Frecuencia')
plt.xlabel('Esperanza de vida')
# Guardamos el gráfico en formato svg
plt.savefig('hist_America.svg')
# Terminamos con el gráfico
plt.show()

# HISTOGRAMA CON LOS DE ÁFRICA Y ORIENTE MEDIO
# Creamos el histograma
plt.hist(AfMe_life_exp, edgecolor = 'black', color = '#568AE4', bins = 15)
# Añadimos un título
plt.title('Figura 3. Frecuencia de la esperanza de vida\nen África y oriente medio en 2019')
# Añadimos nombre a los ejes
plt.ylabel('Frecuencia')
plt.xlabel('Esperanza de vida')
# Guardamos el gráfico en formato svg
plt.savefig('hist_AfMe.svg')
# Terminamos con el gráfico
plt.show()



# Eiliminamos los registros que no sean países
df_paises = df_total.dropna(subset = ['Region'])

# Guardamos los datos de las regiones agrupándolos
cantidad_paises_region = df_paises.groupby(['Region']).size()

# Calculamos el total de países
total_paises = cantidad_paises_region.sum()

# Calculamos el porcentage de paises en cada región
porcentaje_paises_region = (cantidad_paises_region / total_paises) * 100
porcentaje_paises_region = round(porcentaje_paises_region, 0)

# DIAGRAMA DE BARRAS EL NÚMERO DE PAÍSES DE LAS DISTINTAS REGIONES
# Lista de los valores en el eje x de la gráfica
regiones = df_paises['Region'].unique()
regiones = ['LaTam y Caribe', 
            'SudAsia',
            'Sub-Saharan Africa',
            'Europe & Central Asia',
            'Middle East & North Africa',
            'East Asia & Pacific',
            'North America']


# Dibujamos el gráfico
plt.barh(regiones, porcentaje_paises_region, edgecolor = 'black')
plt.savefig('bar_countries.svg')
plt.show()






