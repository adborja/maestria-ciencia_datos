#!/bin/bash
# Mostrar a partir de la linea 2 | ordenar por la columna 2 (emp.id) y columna 9 (birthdate)
# Generar el archivo $1 como resultado
tail +2 ~/work/maestria/2018-I/ciencia_datos/git-repos/Bash-for-data-science/ejercicios/employee | sort -t"," -k2 -g -k9 > $1
