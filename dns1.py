#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver

def main():
    consultas=['A','AAAA','NS','SOA','MX','MF','TXT']
    for c in consultas:
        try:
            a=dns.resolver.query("target_website",c)
            for q in a:
                print(q)
        except:
            print("no pude obtener la consulta")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()