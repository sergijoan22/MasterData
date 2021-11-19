# 12nov_prueba1

import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos

# Listas de prueba
name = ['Yaling', 'Sofia', 'Maria', 'Pablo', 'Inés']
age = [28, 23, 25, 23, 25]
gender = ['Female', 'Female', 'Female', 'Male', 'Female']

# Creamos un dataframe con las listas
# Definimos los nombres de las columnas y que listas usamos para el df
class2021 = pd.DataFrame({'name': name, 'age': age, 'gender': gender})                

# Borramos las listas ya que no nos interesa
# Así desaparecen del explorador de variables
del(age, gender, name)

#Del dataframe
# Mostrar dimensionalidad
class2021.shape
# Mostrar 3 primeras lineas
class2021.head(3)
# Mostrar laas dos ultimas lineas
class2021.tail(2)

# Sacamos del df una columna que se guarda en un objeto llamado series
edad = class2021.age

# Borramos la columna
del(edad)

# Obtenemos el directorio actual del archivo, donde se guardan las cosas
os.getcwd()

# Cambiar el working directory, donde guarda las cosas
# Ponemos r delante para poner el string como raw
os.chdir(r'D:\Master\AnalisisDatos\Ejercicios\12_nov_1')

# Comprobamos que el directorio lo hemos cambiado
os.getcwd()

# Guardamos el df en csv en el directorio por defecto
class2021.to_excel('class2021.xlsx')

# Guardamos el df en excel en el directorio por defecto
class2021.to_csv('class2021.csv')

# Hacer un histograma de la series age
class2021.age.hist()
























































































































































