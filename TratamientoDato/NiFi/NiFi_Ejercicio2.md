## Ejercicio 2

Vamos a traer los datos del ayuntamiento de Valencia mediante una API, para ello usamos el componente InvokeHTTP. En properties, añadimos la URL de la que savar los datos en properties: https://mapas.valencia.es/lanzadera/opendata/Ejes_calle_txt/CSV. En Configuración/scheduling ponemos que busque cada 30 s con run schedule, para no estar buscando todo el rato.

Ese componente lo vamos a llevar a otro que lo troceara en parte (SplitText). En la conexión entre ellos, conectamos la salida Response de InvokeHTTP a la entrada de SplitText. En properties de InvokeHTTP, desmarcamos las demás salidas, ya que no se van a usar. En SplitText, ponemos en Conf/Line Split Count = 500, para separar la entrada en archivos de 500 lineas.

Ahora ponemos uno llamado UpdateAttribute. En Conf/Properties le damos al + de arriba a la derecha: La llamamos filename. Ahora se crea un nuevo atributo en el que ponemos: `EDEM-${filename}-${nextInt()}.txt`, que cambiara los nombres de los ficheros a partir del nombre del original, y poniendo un número a cada uno. Lo conectamos a la entrada split de SplitText, los demás entradas las desconectamos.

Luego lo conectamos a PutFile para guardarlo en el directorio de destino. Elegimos el directorio en este caso `tmp/out` y lo conectamos a la salida splits de SplitText. Las salidas de PutFile las cerramos.

Ahora boton derecho en el fondo, le damos a Start. En el directorio `tmp/out` deben aparecer los archivos.

Para hacer un process group, arrastrar el icono de la barra superior.

```
Generated Username [5fe8e5f7-8b02-488b-a5ee-22afe74fa2a8]
Generated Password [tcguehOQnVd4A5jl4UMB6BcgNOnHHQQ1]
```

Si le damos en el centro, create template, le ponemos un nombre

Luego en el menu de la derecha en Templates podemos descargarlo. Luego load template para abrirlo