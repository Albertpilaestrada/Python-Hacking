#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from os import path
from progress.bar import Bar

def main():
    if path.exists("diccionario_plugins.txt"):
        w=open("diccionario_plugins.txt",'r')
        w=w.read().split('\n')
        lista=[]
        url="web_objetivo"
        b=Bar("Espere...",max=len(w))

        for plugin in w:
            b.next()
            try:
                p=requests.get(url=url+"/"+plugin)
                if p.status_code==200:
                    final=url+"/"+plugin
                    lista.append(final.split("/")[-2])
            except:
                pass
        b.finish()
        for plugin in list:
            print("Plugin encontrado: {}".format(plugin))
    else:
        print("No se encontro el plugin")

if __name__=="__main__":
    main()