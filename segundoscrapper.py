def main():
	web=open('web.html','r',encoding='utf8')
	inicio='<li>'
	final='</li>'
	for l in web.readlines():
		if inicio in l:
			if not "a href=" in l:
				ini = l.find(inicio)
				ini = ini+len(inicio)
				fin = l.find(final)
				print(l[ini:fin])
			    
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()