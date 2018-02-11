#!/bin/bash

# 1. Obtener los registros despues de la segunda fila 
# 2. obtener la tercera columna (fullname) 
# 3. separar por espacio y obtner apellido
# 4. obtener apellido despues del separador "
tail +2 $1 |cut -d',' -f3 |cut -d' ' -f2 |cut -d'"' -f1