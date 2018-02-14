#!/bin/bash

# 1. Agregar 0 a los numeros de mes con un solo digito
cut -d',' -f2 $1 |sed 's/\/\([0-9][\/]\)/\/0\1/' > format_month.tmp

# 2. Agregar 0 a los numeros de dia con un solo digito. (^) significa primer caracter en la linea
sed 's/^\([0-9][\/]\)/0\1/' format_month.tmp > format_date.tmp

# 3. Sustituir / por -
sed 's/\//-/g' format_date.tmp > replace_dash.tmp

# 4. Marcar el campo year
sed 's/\([0-9][0-9][0-9][0-9]\)/year\1/' replace_dash.tmp > mark_year.tmp

# 5. Marcar el campo dia
sed 's/\(^[0-9][0-9][-]\)/day\1/' mark_year.tmp > mark_day.tmp

# 6. Marcar el campo mes
sed 's/-\([0-9][0-9]\)/-month\1/' mark_day.tmp > mark_month.tmp

# 7. Intercambiar 
sed 's/day\([0-9][0-9]\) year\([0-9][0-9][0-9][0-9]\)/\1 \2 \1-\2/' mark_month.tmp > test.tmp

cat test.tmp