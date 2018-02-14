import os

for i in os.listdir('C:/Windows/System32'):
	if i[-3:] == 'exe' or i[-3:] == 'msi':
		print i