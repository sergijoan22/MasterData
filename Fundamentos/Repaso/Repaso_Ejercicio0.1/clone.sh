#!/bin/bash

git clone https://github.com/sergijoan22/MasterDataEDEM.git

touch MasterDataEDEM/hola.txt
echo Hola que pasa > MasterDataEDEM/hola.txt

cd MasterDataEDEM

git add *

git commit –m “Se ha añadido el archivo hola.txt”

git push -u origin
