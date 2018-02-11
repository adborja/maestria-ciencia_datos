#!/bin/bash

# Obtener la primera linea, pasar de mayusculas a minusculas y generar un archivo temporal con el resultado
head -n 1 $1 |tr '[:upper:]' '[:lower:]' > lower.tmp

# Generar un archivo temporal con las lineas a partir de la segunda linea
tail +2 $1 > result.tmp

# Concatenar los archivos temporales
cat lower.tmp result.tmp

# Eliminar los archivos temporales
rm lower.tmp result.tmp