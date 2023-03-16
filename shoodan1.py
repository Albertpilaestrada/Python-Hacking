from shodan import Shodan

key="API Key"

motor=Shodan(key)
try:
    query=motor.search("struts")
    print("Total de resultados: {}".format(query['total']))
    for host in query['matches']:
        print("IP: {}".format(host['ip_str']))
        print("Puerto: {}".format(host['port']))
        print("ORG: {}".format(host['org']))
        try:
            print("ASN: {}".format(host['asn']))
        except:
            pass
        for l in host['location']:
            print(l+""+str(host['location'][l]))
        
except:
    print("ocurrio un error")