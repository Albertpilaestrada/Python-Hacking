from subprocess import check_output
import subprocess

a=check_output('systeminfo',stderr=subprocess.STDOUT,encoding='cp1252')

n=open('informaciondelsistema.txt','w+')
n.write(a)
print("Hola")
n.close()
