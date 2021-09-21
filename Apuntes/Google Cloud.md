# Google Cloud

## Introducción

El Cloud ofrece varios servicios:

- **IAAS**: Infraestructura como servicio.
- **PAAS**: Plataforma como servicio.
- **SAAS**: Software como servicio.

Para comenzar el servicio en la nube, hay que registrarse en Google Cloud Platform. Google Cloud cobra por tiempo, independientemente del uso que se le de a la máquina.

En el menú de la izquierda: Compute engine -> Instancias de vm. Creamos una instancia y la configuramos: 

- Le ponemos un nombre que queramos.
- Elegimos la región más cercana, en este caso Londres. Se puede elegir cualquier región pero las más cercanas ofrecen mejor conexión.

- Elegimos la serie N1.
- En el tipo de máquina elegimos f1-micro, ya que es la máquina con menos memoria, siendo más que suficiente.
- Elegimos como SO Debian para poder practicar los comandos en Linux, aunque otra distribución también serviría.

Una vez creada la instancia, hacemos la conexión con el protocolo SSH, abriendo el terminal en otra ventana del navegador. Se nos abre en la ventana un terminal Linux en el que se pueden usar los comandos pero no somos administradores.

Una vez hemos acabado de usar la instancia, en el símbolo de los tres puntos se debe detener o borrar.
