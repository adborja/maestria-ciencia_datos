#!/bin/bash
# Obtener los registros desde la segunda fila | Obtener la columna 3 (supplier.id) | ordenar | eliminar repetidos | contar lineas
tail +2 $1 |cut -d',' -f3 |sort -g |uniq |wc -l