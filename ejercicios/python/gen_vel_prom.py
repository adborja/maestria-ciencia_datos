import glob
import re
from collections import defaultdict

def groupByStationHour(source_file):
	dic = defaultdict(list)
	# Recorrer el archivo linea por linea
	isFirstLine = True

	for line in source_file:
		## Ignorar primera linea
		if isFirstLine:
			isFirstLine = False
			continue

		campos = line.split(',')
		clave = campos[0] + '-' + campos[1] + '-' + campos[5].split(':')[0]
		velocidad = campos[-1]
		dic[clave].append(float(velocidad))
	return dic

def getAvgByStation(mymap):
	for key in mymap.keys():
		count = len(mymap[key])
		suma = sum(mymap[key])
		mymap[key] = suma / count
	return mymap

def genFiles(avgMap):
	header = 'ESTACION,ANO,MES,DIA,HORA,PROM'

	for key in avgMap.keys():
		filename = key + '.txt'
		file_out = open(filename, 'a')

		data = key + ',' + str(avgMap[key]) + '\n'

		file_out.write(header + '\n')
		file_out.write(data.replace('-',','))
		file_out.close()


source_file = open("tmp_all_stations.csv", 'r')
mydic = groupByStationHour(source_file)
result = getAvgByStation(mydic)
genFiles(result)
source_file.close()
