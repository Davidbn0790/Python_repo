import os

def version():
	return '1.0.0'

#Crear una funcion que intente crear un directorio. Si existe que de un error de que no existe, si no existe, que cree el directorio

def creadir(path):
	if not os.access(path,os.R_OK):
		os.mkdir(path)
		return 'Directorio creado'
	else:
		return 'El directorio ya existe'
