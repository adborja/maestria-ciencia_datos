import pandas as pd

def csv_to_html(source_filename, target_filename):
	dataframe = pd.read_csv(source_filename, sep = ';', thousands = None, decimal = '.')
	dataframe.to_html(target_filename, index = False)

def html_to_csv(source_filename, target_filename):
	dataframe = pd.read_html(source_filename)
	dataframe[0].to_csv(target_filename, sep = ';', index = False)

	
source1_filename = 'taller1_1_customers.csv'
target1_filename = 'taller1_1_customers.html'
source2_filename = 'taller1_3_customers.html'
target2_filename = 'taller1_3_customers.csv'

csv_to_html(source1_filename, target1_filename)
html_to_csv(source2_filename, target2_filename)
