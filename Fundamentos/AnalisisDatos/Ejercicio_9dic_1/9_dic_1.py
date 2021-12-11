


import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


# Change working directory
os.chdir('D:\Master\AnalisisDatos\Ejercicio_9dic_1')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK


##############################################################################

#Comenzamos describiendo la temperatura

temp = wbr['temp_celsius']
plt.hist(temp, bins = 10, edgecolor = 'black')

# Tambien se deberia hacer con rentals que es lo que vamos a analizar 

# Ahora un scatter plot
plt.scatter(wbr.temp_celsius, wbr.cnt, facecolors = 'none', edgecolors = 'C0')
plt.xlabel('Temp (Centigrades)')
plt.ylabel('Daily rentals')

# Vamos a analizar la correlacion
from scipy.stats import pearsonr

pearsonr(wbr.temp_celsius, wbr.cnt)

# Nos da el ceoficiente de correlacion linal de person 
# El segundo numero es es el pvalue
# Al ser tan bajo nos permite afirmar con seguridad que hay correlacion

r, p_val = pearsonr(wbr.temp_celsius, wbr.cnt)
n = len(wbr.cnt)

# Lo dibujamos añadiendo los datos obtenidos
# Ponemos por año un color diferente
plt.figure(figsize = (5, 5))
plt.scatter(wbr.temp_celsius, wbr.cnt, facecolors = 'none', c = wbr.yr)
plt.xlabel('Temp (Centigrades)')
plt.ylabel('Daily rentals')
plt.title('Daily bicycle rentals, by temperature')
props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

# Se ve para altas temperaturas, hay diferencia de rentals entre ambos años. Se debe
# a que se puso el segundo año mas estaciones.


# Ahora vamos a hacer lo mismo pero dibujando los puntos dependiendo
# de la estacion
plt.figure(figsize = (5, 5))
plt.scatter(wbr.temp_celsius, wbr.cnt, facecolors = 'none', c = wbr.season)
plt.xlabel('Temp (Centigrades)')
plt.ylabel('Daily rentals')
plt.title('Daily bicycle rentals, by temperature')
props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

##################################################################################

# Ahora, en vez de la temperatura se va a hacer con el viento
# Primero se describe
plt.hist(wbr.windspeed_kh, bins = 10, edgecolor = 'black')

# Se hace el test
pearsonr(wbr.windspeed_kh, wbr.cnt)

# Se guardan los datos para usarlos luego
r, p_val = pearsonr(wbr.windspeed_kh, wbr.cnt)
n = len(wbr.cnt)

# Hacemos el dibujo
plt.figure(figsize = (5, 5))
plt.scatter(wbr.windspeed_kh, wbr.cnt, facecolors = 'none', edgecolors = 'C0')
plt.xlabel('Wind speed (kh)')
plt.ylabel('Daily rentals')
plt.title('Daily bicycle rentals, by wind speed')
props = dict(boxstyle = 'round', facecolor = 'white', lw = 0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, p_val, n)
plt.text (3,7000, textstr , bbox=props)
plt.show()

# Se puede apreciar que no hay relacion entre ambas, tal y como dice la r de person












