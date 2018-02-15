import paquetes.ficheros
import sys
#print paquetes.ficheros.creadir('/tmp/prueba')

if len(sys.argv) <> 2:
	print "Funcion de programa: ejercicio_14.py <directorio_a_crear>"
else:
	print paquetes.ficheros.creadir(sys.argv[1])
