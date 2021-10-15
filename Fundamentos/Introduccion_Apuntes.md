# Introducción

## Encoding

Bits para definir un carácter. Por ejemplo:

- UTF-8: Necesitas 8 bits para escribir una palabra
- UTF-16: Necesitas 16

A más bits más caracteres pueden poner en el diccionario

Un ejemplo es ASCI

## Comunicación Cliente – Servidor

**API**: Función que ofrece un servidor

**Rest**: Manera de convocar una API

A la hora de establecer comunicación, el código 200 indica que ha ido todo perfecto y uno distinto que no.

## Lenguajes de programación

**Compilado**: Convierte el código a binario para que lo lea el SO (C++)

**Interpretado:** Se necesita un programa que lea y ejecute el código cada vez (Python)

**Intermedio:** Mezcla de ambos (Scala)

## Log

Como un ordenador nos dice lo que está pasando. Archivo de texto que informa de errores, cambios, etc.

## Encriptación

Hay claves públicas y privadas. La pública cifra un archivo y la privada también la descifra (Esta nunca se comparte). Al enviar un archivo a otro, se cifra con una llave pública.

Programa para generar claves: https://www.puttygen.com/download-putty

Descargar putty.zip de x64 y al descomprimir abrir Puttygen.exe, dar a generar, se crea una clave pública aleatoria y ponemos una contraseña. Le damos a guardar las claves público y privado y obtenemos dos archivos por separado.

## Protocolos

Métodos de comunicación entre procesos.

**SSH:** Para ejecutar comandos.

**HTTP:** Protocolo web.

**FTP/SFTP:** Para enviar archivos.

## Filezilla

Programa de transferencia de archivos que usa los protocolos FTP y SFTP.

Vamos a hacer una conexión de prueba:

- Servidor: test.rebex.net

- Nombre de usuario: demo

- Contraseña: password

- Puerto: 22


Se introducen los datos en el menú principal de Filezilla y tenemos acceso a los archivos de un servidor externo. 

## Putty

Programa para establecer conexión con el protocolo SSH. Para realizar la conexión al servidor de antes, se especifica el nombre del servidor y el puerto para hacer una conexión SSH. Al conectarse accedemos a un terminal que pide el usuario y la contraseña para poder acceder al servidor mediante el terminal con Linux.

## Puerto

Se definen mediante 16 bits y hay abiertos y estándar. Los distintos protocolos tienen un puerto reservado para ellos, por ejemplo:

HTTP: Puerto 80.

FTP: Puerto 20.

SSH: Puerto 22.

SFTP: Puerto 443.

Podemos entrar a una página web como marca.com sin indicar puerto y usa el de por defecto (80 al ser HTTP), o podemos indicarlo manualmente.

En FTP respecto a SFTP la información no va cifrada. No puedes ir al puerto 22 con información cifrada.

## CPU/GPU/TPU

TPU está pensado para TensorFlow, un lenguaje para data.

## Sistema operativo

Intermediario entre usuario y hardware: Usuario <> Aplicación <> SO <> Hardware

