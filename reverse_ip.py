#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

def main():
    sitio="traget_web_server"
    agent={'User-Agent':'Fireox'}
    a=requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(sitio),headers=agent)
    b=BeautifulSoup(a.text,'html5lib')
    c=b.find(id="null")
    d=c.find(border="1")
    for l in d.find_all("tr"):
        print("Sitio encontrado: "+l.td.string)


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()