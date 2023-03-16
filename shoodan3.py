from shodan import Shodan
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-q','--query',help="Busqueda")
parser.add_argument('-a','--api',help="Tu api")
parser = parser.parse_args()

def main():
	if parser.query:
		
		if parser.api:
			
			api = Shodan(parser.api)

			try:
				b = api.search(parser.query)
				print("Total de objetivos: {}".format(b['total']))
				for i in b['matches']:
					print("Target encontrado: {}".format(i['ip_str']))
			except:
				print("Error en la consulta")
		else:
			print("Introduce tu api key")

	else:
		print("Introduce un caractar de Busqueda")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()