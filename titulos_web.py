def main():
	files=open('web.html','r',encoding='utf8')
	inicio='<title>'
	final='</title>'
	for l in files.readlines():
		if inicio in l:
			p=l.find(inicio)
			print(l[p+len(inicio):-len(final)-1])
				
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()