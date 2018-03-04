"""
Este es un demo de documentacion

>>> hello('juan')
Hola juan desde demotdd.py

"""
def hello(s):
	print('Hola ' + s + ' desde ' + __file__)
	
if __name__ == "__main__":
	# all it ebooks http://www.allitebooks.com/
	import doctest
	doctest.testmod()