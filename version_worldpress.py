import requests
from bs4 import BeautifulSoup

def main():
    url="http://localhost/HTML5/"
    cabecera={'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0'}
    peticion=requests.get(url=url,headers=cabecera)
    #print(peticion.text)
    soup=BeautifulSoup(peticion.text,'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name')==('generator'):
            version=v.get('content')
    print(version)


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
