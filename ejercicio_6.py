#Programa que por teclado se pida una letra y se diga en cuantos nombres de fichero aparece esa letra

import os

num=0
letra=raw_input('Dime letra/s:\n')
print '========================='
lista=os.listdir('C:/Windows/System32')
for i in lista:
	if i.count(letra) > 0:
		print i
		num=num+1

print '========================='
print "Hay " + str(num) + " ficheros que contienen la/s letra/s"