# NiFi

## Data ingestion

Pasar los datos del origen a donde los vamos a usar. Programas para ello, como NiFi, necesarios si hay muchas fuentes de datos.

### Flujo del dato:

Data Ingestion -> ETL -> Análisis

## NiFi

Los datos de origen pasan por un conjunto de procesadores conectados que procesan los datos.

Scalability: Cadacidad de procesar datos si su volumen aumenta

FlowFile: Dato que esta fluyendo.

FlowFile processor: El que manipula el FLowFile

Connection: Lo que conecta dos procesadores

Process group: Agrupación de componentes

Otros porductos complementarios:

minifi es una version mas ligera

NiFi registry es para la gestión de código. Para trabajos en equipo sobretodo.
