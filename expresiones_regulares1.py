import re
from urllib.request import urlopen

def parser3():
	cadena="Esta es una cadena que vamos a usar para usar como ejemplo para otra funcion"
	cadena1=re.sub('funcion','sub',cadena) #sub() reemplaza valores en todo el codigo fuente, cadena de texto o datos extensos 
	print(cadena1)
	
def parser2():
	pagina=open('web.html','r',encoding='utf8')
	for l in pagina.readlines(): #Ejemplo 2 funcion findall() encuentra multiples resultados en cadenas de texto enormes
		b=re.findall('^<html>',l) #^ este caracter al inicio de una palabra, la linea de codigo que vamos a buscar tiene que empezar con esta palabra
		if b:
			print(b)
		b=re.findall('</html>$',l) #$ este caracter al final de una palabra, la linea de codigo que vamos a buscar tiene que terminar con esta palabra
		if b:
			print(b)
		b=re.findall('<li>.*</li>',l) #.* indica que voy a buscar todo dentro de las palabras que estan antes y despues
		if b:
			for c in b:
				d=re.split('<li>',c) # la funcion split() nos permite cortar un elemento
				print(d)
			    
def parser1():
	pagina=open('web.html','r',encoding='utf8')
	for l in pagina.readlines():
		b=re.search('lorem',l) #Ejemplo 1 usa la funcion search() nos devuelve un objeto para verificar si la busqueda es encontrada
		if str(b) in l:
			print(l)
		else:
			pass
def main():
	parser1()
	parser2()
	parser3()
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()