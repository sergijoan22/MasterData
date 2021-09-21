# Ejercicio Linux 3

#### En la máquina virtual creada en Google Cloud instala Git.

`sudo apt update`

`sudo apt-get install git`

#### Crea un archivo script.h con permisos de ejecución.

`cd /home/sergi98lapunta`

`touch script.sh`

#### Añade un código Bash en el archivo que calcule y devuelva 5\*1+5\*2+5\*3...5\*100

````bash
#!/bin/bash
a=5
b=0
for i in 'seq 1 100';
do
	b=$(( $b + $(( $i * $a))))
done
echo $b
````

Una vez creado el archivo, para ejecutarlo se usa el comando sh.

`sh script.sh`
