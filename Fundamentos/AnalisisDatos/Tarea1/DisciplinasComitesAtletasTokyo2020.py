# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:28:22 2021

@author: sergi
"""

# Importamos las librerías necesarias
import os # Sistema operativo
import pandas as pd # Datasets
import numpy as np # Vectores, matrices
import matplotlib.pyplot as plt # Hacer gráficos

# Leemos archivo con los atletas de tokyo2020
df_atletas = pd.read_excel('atletas.xlsx')

# Agrupamos por la disciplina y el comité olímpico de los atletas
comite_atletas = df_atletas.groupby(['NOC']).size()
disciplina_atletas = df_atletas.groupby(['Discipline']).size()

# Ordernamos de mayor a menor
comite_atletas = comite_atletas.sort_values(ascending = False)
disciplina_atletas = disciplina_atletas.sort_values(ascending = False)

# Contamos el total de atletas
total_atletas = comite_atletas.sum()


# Pasamos las tablas de disciplinas y comités a porcentajes
comite_atletas = (comite_atletas / total_atletas) * 100
disciplina_atletas = (disciplina_atletas / total_atletas) * 100

# Nos quedamos con las 10 disciplinas y comiés más comunes
comite_atletas = comite_atletas.head(5)
disciplina_atletas = disciplina_atletas.head(5)

# Redondeamos los cifras
comite_atletas = round(comite_atletas, 0)
disciplina_atletas = round(disciplina_atletas, 0)

# Pasamos los datos a excel para hacer una tabla
comite_atletas.to_excel('comite_atletas.xlsx')
disciplina_atletas.to_excel('disciplina_atletas.xlsx')

# Hacemos ahora el diagrama de barras para los comités
bar_list = comite_atletas.index.tolist()
plt.bar(bar_list, comite_atletas, edgecolor = 'black')
plt.ylabel('Porcentaje de atletas')
plt.title('Figura 2. Porcentaje de atletas en los países principales')
plt.savefig('comite_atletas.svg')
plt.show()

# Hacemos ahora el diagrama de barras para las disciplinas
bar_list = disciplina_atletas.index.tolist()
plt.bar(bar_list, disciplina_atletas, edgecolor = 'black')
plt.ylabel('Porcentaje de atletas')
plt.title('Figura 1. Porcentaje de atletas en las disciplinas principales')
plt.savefig('disciplina_atletas.svg')
plt.show()

