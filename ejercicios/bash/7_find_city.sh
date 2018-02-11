#!/bin/bash
# Obtener los registros despues de la linea 2 (Ignorar nombres de columnas) | obtener solo la columnas 1 (cust.id), 4 (fullname) y 3 (city) | buscar la palabra $2
tail +2 $1 |cut -d ',' -f1 -f4 -f3 |grep $2
