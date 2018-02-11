#!/bin/bash
# Mostrar la 3 columna (-f3) de la ultima linea de $1 (tail -n 1)
tail -n 1 $1 | cut -d ',' -f3

