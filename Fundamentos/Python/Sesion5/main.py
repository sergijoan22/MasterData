import pandas as pd

# LEER CSV
# Con dtype podemos especificar el tipo de datos de cada columna, si en un int hay un valor decimal lo convertirá
pokemon_df = pd.read_csv('pokemon_data.csv', dtype = {'Name': str, 'Type 1': str, 'Speed': int, 'Generation': str, })

# EXCEL
#pokemon_df_excel = pd.read_excel('pokemon_data.xlsx')

# TXT CON TABULACIÓN
#pokemon_df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t')

# Mostrar 10 primeras filas
print(pokemon_df.head(10))

# Mostrar 5 últimas filas
print(pokemon_df.tail(5))

# Obtener los nombres de las columnas
print(pokemon_df.columns)

# Obtener todos los valores de la columna name
print(pokemon_df['Name'])

# Obtener todos los valores de las columnas name y speed
print(pokemon_df[['Name', 'Speed']])

# Obtener los 12 primeros nombres de la columna name (también se puede usar head())
print(pokemon_df['Name'][:12])

# Obtener fila (Se guarda como un diccionario o una lista de diccionarios)
print('Fila 0')
print(pokemon_df.iloc[0])

# Obtener las 5 primera filas
print(pokemon_df.iloc[0:6])

# Obtener el valor de una celda. En este caso, el valor de la fila 0, columna 1. Dos modos
print(pokemon_df.iloc[0][1])
print(pokemon_df.iloc[0, 1])

# Iterar por todos y mostrar el índice y nombre de cada
for i, pokemon in pokemon_df.iterrows():
    print(i, pokemon['Name'])

# Encontrar todos los pokemon que de tipo1 sean agua
print('\n\nTIPOS AGUA\n\n')
pokemons_agua = []
for i, pokemon in pokemon_df.iterrows():
    if pokemon['Type 1'] == 'Water':
        pokemons_agua.append(pokemon['Name'])
print(pokemons_agua)

# Forma mas limpia de hacer lo mismo
print(pokemon_df.loc[pokemon_df['Type 1'] == 'Water'])

# Mostrarlos ordenados por orden
print(pokemon_df.sort_values('Name', ascending = True))

# Mostrarlos ordenados por tipo 1 de forma ascendente y si no por HP de forma descendente. Mostrar solo 3 columnas
print(pokemon_df.sort_values(['Type 1', 'HP'], ascending = [True, False])[{'Name', 'Type 1', 'HP'}])

# Añadir una columna llamada total a partir de otras columnas
pokemon_df['Total'] = pokemon_df['HP'] + pokemon_df['Attack'] + pokemon_df['Defense'] +pokemon_df['Speed']

# Mostrar la nueva columna creada
print(pokemon_df['Total'])

# Encontrar los 5 mejores pokemon a partir de la columna total
print(pokemon_df.sort_values('Total', ascending = False)[{'Name', 'Total'}].head(5))

# Eliminar la columna total
pokemon_df = pokemon_df.drop(columns = ['Total'])
print(pokemon_df)

