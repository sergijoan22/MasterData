# Ejercicio Linux 2

#### De la máquina virtual creada en Google Cloud, ¿Cuáles son los ficheros y directorios presentes en el directorio raíz?

`cd /`

`ls`

#### ¿Cuáles son todos los archivos presentes en nuestro directorio de usuario?

`cd home/sergi98lapunta`

`ls -l`

#### Crea un directorio llamado experimento en nuestro directorio de usuario.

`mkdir experimento`

#### Crea con touch los archivos datos1.txt y datos2.txt dentro del directorio experimento.

`cd experimento`

`touch datos1.txt`

`touch datos2.txt`

#### Vuelve al directorio principal de tu usuario y desde allí lista los archivos presentes en el directorio experimento usando rutas absolutas y relativas.

`cd ..`

`ls -l /home/sergi98lapunta`

`ls -l`

#### Borra todos los archivos que contengan un 2 en el directorio experimento.

`cd experimento`

`rm *2*`

#### Copia el directorio experimento a un nuevo directorio llamado exp_seguridad.

`cd ..`

`cp -r experimento exp_seguridad `

#### Borra el directorio experimento.

`rm -rf experimento`

#### Renombra el directorio exp_seguridad a experimento.

`mv exp_seguridad experimento`

#### Copia el fichero /etc/passwd al directorio experimento.

`cp /etc/passwd /home/sergi98lapunta/experimento`

#### Copia el fichero /etc/passwd al directorio experimento con el nombre usuarios.txt y poner el archivo como solo lectura.

`cp /etc/passwd /home/sergi98lapunta/experimento/usuarios.txt`

`chmod 444 experimento/usuarios.txt`
