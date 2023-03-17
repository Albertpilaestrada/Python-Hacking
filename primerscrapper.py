import urllib
from urllib.request import urlopen

def main():
	file_web=open('web.html','wb')
	consulta=urlopen(url='https://lorem2.com/')
	consulta=consulta.read()
	file_web.write(consulta)
	file_web.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()