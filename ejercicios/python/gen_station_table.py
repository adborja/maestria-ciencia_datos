import glob
import re
import os

##
## Ruta donde se encuentran los archivos Est*.csv
##
source_path = '/Users/adborja/work/maestria/2018-I/ciencia_datos/git-repos/IPython-for-data-science/05-caso-practico'

##
## archivo de salida
##
file_out = open('result.csv', 'w')
  
## se agrega el encabezamiento
file_out.write("ESTACION,FECHA,ANO,MES,DIA,HHMMSS,HORA,MIN,DIR,VEL\n")
    
##
## se recorren todos los archivos *csv en el directorio 
##
for filename in glob.glob(source_path + "/Es*.csv"):
    
    ## abre el archivo para lectura
    file_in = open(filename, 'r')
    
    ## se ignora la primera linea de encabezados
    isfirstline = True
    
    ## se leen una a una las lineas del archivo *csv
    for line in file_in:
        
        ## se ignora la primera linea de encabezados
        if isfirstline is True:
            isfirstline = False
            continue
        
        ##
        ## se agrega el nombre del archivo
        ##
        tmp_filename = os.path.basename(filename)
        line = tmp_filename[:-4] + ';' + line
        
        ##
        ## Se cambian las ',' por '.'
        ##
        line = line.replace(',', '.')
        
        ##
        ## Se cambian los ';' por ','
        ##
        line = line.replace(';', ',')
        
        ##
        ## Se extrae de HH:MM:SS las HH y los MM
        ##
        groups = re.search(',([0-9]+):([0-9][0-9]):([0-9][0-9])', line)
        if groups:
            org_text = groups.group(0)
            new_text = org_text + ',' + groups[1] + ',' + groups[2]
            line = line.replace(org_text, new_text)
        
        ##
        ## Se agrega el 0 al digito del dia
        ##
        groups = re.search(',([0-9])/', line)
        if groups:
            org_text = groups.group(0)
            new_text = ',0' + groups.group(1) + '/'
            line = line.replace(org_text, new_text)


        ## Se cambia el formato DD/MM/YY a YYYY-MM-DD
        ## y agrega las columnas año, mes, dia
        groups = re.search(',([0-9][0-9])\/([0-9][0-9])\/([0-9][0-9])', line)  
        org_text = groups.group(0)
        new_text = ',20' + groups.group(3) + '-' + groups.group(2) + '-' + groups.group(1) 
        new_text +=  ',20' + groups.group(3) + ',' + groups.group(2) + ',' + groups.group(1) 
        
        # print(lineaorg_text, '\n', new_text, sep = '')
        line = line.replace(org_text, new_text)
        
        ##
        ## se escribe la linea modificada al archivo de salida
        ##
        file_out.write(line)
    
    file_in.close()

file_out.close()