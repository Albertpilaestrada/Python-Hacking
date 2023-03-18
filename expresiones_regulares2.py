import re
from urllib.request import urlopen

def get_li():
	code=urlopen('https://lorem2.com/')
	code=code.read()
	todo=re.findall('<li>(.+?)</li>',str(code))
	for t in todo:
		if not "a href=" in t:
		   print(t + '\n')	
	
def main():
	get_li()
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()