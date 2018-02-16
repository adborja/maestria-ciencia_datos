#!/bin/bash
# 1. Buscar un texto con una (,) seguido de un digito y un (/), luego cambiarlo por ,0 + el digito
sed 's/,\([0-9]\/\)/,0\1/' $1 > out1.tmp

# 2. Buscar un texto con un (/) seguido de un digito y un (/), luego cambiarlo por /0 + el digito
sed 's/\/\([0-9]\/\)/\/0\1/' out1.tmp > out2.tmp

# 3. Buscar un texto con una (,) seguido de dos digitos mas un (/) seguido de dos digitos mas un (/)
# seguido de cuatro digitos, intercambiar 3 con 1
sed 's/,\([0-9][0-9]\)\/\([0-9][0-9]\)\/\([0-9][0-9][0-9][0-9]\)/,\3-\2-\1/' out2.tmp > out3.tmp