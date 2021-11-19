	
#Archivo main.py
from utilidades.interacciones.cordialidad import saludar
from utilidades.kpis import puntuacion
 
puntos = puntuacion(4532)
 
print(f'{saludar("Pedro")} tu puntuación es de {puntos}')
