print 'introduce numero inicio'
num1=raw_input()
print 'introduce numero fin'
num2=raw_input()
print '==================='
for numero in range(int(num1),int(num2)):
	if numero %2 == 0:
		print numero