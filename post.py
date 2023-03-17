import requests
import argparse
from os import path

parser = argparse.ArgumentParser(description="detector de cabezeras")
parser.add_argument('-f','--file',help="indica el achivo a subir")
parser = parser.parse_args()

def main():
    if parser.file:
        if path.exists(parser.file):
            archivo=open(parser.file,'rb')
            headers={'User-Agent':'Firefox'}
            peticion=requests.post(url="http://direccion_de_la_pag_donde_vamos_a_subir_el_archivo",files={'Uploaded_file':archivo},headers=headers)
            if parser.file in peticion.text:
                print(peticion.text)
                print("Archivo subido con exito")
            else:
                print("Fallo la subida del archivo")

        else:
            print("no exite el archivo")    
    else:
        print("necesito un archivo para subir")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
