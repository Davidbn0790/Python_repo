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

#Funcion llamada entorno que devuelva el usuario, la shell y el path de la sesion activa

def entorno():
	entorno=os.environ
	print entorno['USER']
	print entorno['PATH']
	print entorno['SHELL']
	print "========\nAhora con un for\n========="
	for i,x in os.environ.iteritems():
		if i == 'USER' or i == 'SHELL' or i == 'PATH':
			print i + " = "+ x

#Funcion en la que devuelva los ficheros de un directorio que ocupen mas de un size que se introduzca

def gordos(path,size,type):
	if type == 'K':
		size = int(size)*1024
	if type == 'M':
		size = int(size)*1024*1024
	if type == 'G':
		size= int(size)*1024*1024*1024
	for i in os.listdir(path):
		file=path+i
		#print file
		#print os.path.getsize(file)
		if os.path.isfile(file) and os.path.getsize(file) > int(size):
			sizef=os.path.getsize(file)
			if type == 'K':
				sizef=os.path.getsize(file)/1024
				print "fichero " + str(file) + " // " + str(sizef) + "K"
			if type == 'M':
				sizef=os.path.getsize(file)/1024/1024
				print "fichero " + str(file) + " // " + str(sizef) + "M"
			if type == 'G':
				sizef=os.path.getsize(file)/1024/1024/1024
				print "fichero " + str(file) + " // " + str(sizef) + "G"

#Funcion que muestre el contenido de un fichero	

def visualizar(fichero):
	file=open(fichero,'r')
	file1=file.read()
	#file2=file.readlines()
	#print file2
	print file1
	file.close()
