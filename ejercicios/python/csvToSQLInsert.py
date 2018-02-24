import glob
import os

def lineToSQLInsert(header, table, line):
	header = header.replace('\n', '\0')
	# line separado por ;
	header = header.replace(';', ',')
	line = line.replace('\n', '\0')
	# line separado por ;
	arr_values = line.split(';')

	sql = 'INSERT INTO ' + table + ' (' + header + ')' + ' VALUES (' + "'" + arr_values[0] + "'" + ',' + "'" + arr_values[1] + "'" + ',' + "'" + arr_values[2] + "'"');'
	return sql

def csvToSQL(csv_file, sql_file, table):
	header = ''
	# Obtener cabecera
	isFirstLine = True
	for line in csv_file:
		if isFirstLine:
			header = line
			isFirstLine = False
			continue
		sql = lineToSQLInsert(header, table, line)
		sql_file.write(sql + '\n')


# Invocar funcion csvToSQL
table = 'customer'
source_file = open('taller1_1_customers.csv', 'r')
file_out = open('customers.sql', 'a')
csvToSQL(source_file, file_out, table)

file_out.close()
source_file.close()