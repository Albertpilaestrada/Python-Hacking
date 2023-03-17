import json
import urllib
from urllib.request import urlopen

def main():
    url="https://ipinfo.io/target_ip/json"
    v=urlopen(url)
    j=json.loads(v.read())

    for dato in j:
        print(dato+" : "+ j[dato])


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
