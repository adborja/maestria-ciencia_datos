#!/bin/bash
# Mostrar a partir de la linea 2 | ordenar por la columna 3 (nombre) | cortar la columna 3 (nombre)
# Generar el archivo $1 como resultado
tail +2 ~/work/maestria/2018-I/ciencia_datos/git-repos/Bash-for-data-science/ejercicios/employee | sort -t"," -k3 | cut -d ',' -f3 > $1
