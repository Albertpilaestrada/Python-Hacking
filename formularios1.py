import mechanize
import argparse
from bs4 import BeautifulSoup

parser=argparse.ArgumentParser()
parser.add_argument("-b",'--buscar',help="opcion a buscar")
parser=parser.parse_args()


def main():
    if  parser.buscar:
        bus=mechanize.Browser()
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.addheaders=[('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]
        bus.open("https://www.google.com")
        for n in bus.forms():
            print(n)
        bus.select_form(nr=0)
        bus['q']=parser.buscar
        bus.submit()
        #print(bus.response().read())
        p=BeautifulSoup(bus.response().read(),'html5lib')
        for link in p.find_all('a'):
            u=(link.get('href'))
            u=u.replace('/url?q=','')
            print(u)
            

        #for n in bus.forms():
            #print(n)
    else:
        print("Palara a buscar")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
