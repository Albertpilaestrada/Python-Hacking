#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket

s=socket.socket()
try:
    s.connect(("scanme.nmap.org",22))
    banner=s.recv(1024)
    print(banner)
except:
    print("Ocurrio un error en la conexion")