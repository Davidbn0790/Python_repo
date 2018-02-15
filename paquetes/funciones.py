def imprimir():
	print 'Mi primer print'
	
def imprimir_retorno():
	return 'Hola Mundo'
	
def parimpar(num):
	return "par" if (int(num)%2==0) else "impar"

#	if int(num)%2 == 0:
#		print 'par'
#	else:
#		print 'impar'

#Funcion que recibe DNI, NOMBRE y APELLIDOS

def acliente(dni, nombre, *apellidos):
	print 'DNI: ' + dni
	print 'Nombre: ' + nombre
	print 'Tienes ' + str(len(apellidos)) + ' apellidos'
	print 'Apellidos:'
	for x in apellidos:
		print x
		
#Funcion que devuelve las iniciales del nombre y apellidos que pongas

def iniciales(nombre, *apellidos):
	
	inic=nombre[0] + '.'
	for i in apellidos:
		inic = inic + i[0] + '.'
	return inic