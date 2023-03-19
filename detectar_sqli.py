import mechanize
from bs4 import BeautifulSoup

nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders = [('User-Agent','Firefox')]
nav.open("http://127.0.0.1:42001/index.php")
nav.select_form(nr=0)

nav['username'] = 'admin'
nav['password'] = 'password'

nav.submit()

nav.open("http://127.0.0.1:42001/vulnerabilities/sqli/")
nav.select_form(nr=0)

nav['id'] = '1'

nav.submit()
soup = BeautifulSoup(nav.response().read(),'html5lib')
print(soup)