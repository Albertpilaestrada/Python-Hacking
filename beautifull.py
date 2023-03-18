import requests
from bs4 import BeautifulSoup

def main():
	user_agent={'User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0'}
	url=requests.get(url="http://localhost/HTML5/")
	if url.status_code==200:
		datos=BeautifulSoup(url.text,'html.parser')
		datos1=datos.find_all('img')
		for n in datos1:
			if n.get('title') is not None:
				print(n.get('title').encode('utf-8'))
		
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()