#!/bin/bash

# 1. Ordenar el archivo de empleados por ID
# 2. Ordenar el archivo de clientes por ID
# 3. Unir los empleados y clientes por ID mostrando emp.fullname y cus.fullname
# 4. Unir el resultado con ordenes
sort -t',' -k2 -g $1 > sorted_emp.tmp
sort -t',' -k1 -g $2 > sorted_cus.tmp
join -t',' -1 2 -2 1 -o"0 1.3 2.4" sorted_emp.tmp sorted_cus.tmp > joined_emp_cus.tmp
join -t',' -1 1 -2 1 joined_emp_cus.tmp $3

# Eiminar archivos tmp
rm sorted_emp.tmp sorted_cus.tmp joined_emp_cus.tmp