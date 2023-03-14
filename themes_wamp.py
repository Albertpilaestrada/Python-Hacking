#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

def main():
    agent={'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0'}
    peticion=requests.get("http://localhost/")
    soup=BeautifulSoup(peticion.text,'html5lib')
    for enlace in soup.find_all('link'):
        if 'wampthemes/' in enlace.get('href'):
            them=enlace.get('href')
            them=them.split('/')
            print(them)
            if 'wampthemes' in them:
                pos=them.index('wampthemes')
                theme=them[pos+1]
                print("Tema en uso " + theme) 


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()