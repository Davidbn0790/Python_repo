#Conectarse en remoto y hacer ls de un directorio.

import sys, paramiko

command=sys.argv[1]


client=paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy)
client.set_missing_host_key_policy(paramiko.WarningPolicy)

client.connect('192.168.1.59', port='22', username='oracle', password='oracle')

stdin,stdout,stderr=client.exec_command(command)

print stdout.read()

client.close()
