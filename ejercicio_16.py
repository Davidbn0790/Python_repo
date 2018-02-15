import sys

import paquetes.ficheros 

if len(sys.argv)<>4:
	print "Uso del programa: programa.py <path> <size> <tipo>"
else:

	if sys.argv[3] in ('K','M','G'):
		paquetes.ficheros.gordos(sys.argv[1],sys.argv[2],sys.argv[3])
	else:
		print "Solo valen los valores K, M, G"
