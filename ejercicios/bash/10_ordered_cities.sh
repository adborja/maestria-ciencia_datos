#!/bin/bash
# Obtener los registros a partir de la segunda linea | Obtener la columna 2 (city) | ordenar | eliminar duplicados
tail +2 $1 |cut -d',' -f3 |sort |uniq