import sys
from shodan import Shodan
import importlib

importlib.reload(sys)
#sys.setdefaultencoding('utf8')

def main():
	api = Shodan('xkrPkijqTbScUlonmYkHVIRrHYUUZX0a')
	h = api.host('117.48.120.228')
	print('''

		Direccion: {}
		Ciudad: {}
		ISP: {}
		Org: {}
		Puertos: {}

		'''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['ports']))

	file = open('escaneo.txt','a+')

	for elemento in h['data']:
		lista = elemento.keys()
		for l in lista:
			file.write(str(elemento[l]))

	file.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
