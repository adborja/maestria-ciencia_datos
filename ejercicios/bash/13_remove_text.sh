#!/bin/bash

# Eliminar las filas que contienen un texto $1 y crear un backup del archivo
sed -i.bak "/$1/d" $2