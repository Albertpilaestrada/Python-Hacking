import requests

def main():
    word="cloudflare"
    url=requests.get("target_website")
    cabeceras=dict(url.headers)
    verify=False
    for c in cabeceras:
        if word in cabeceras[c].lower():
            verify=True
            break

    if verify==True:
        print("Cloudflare presente")
    else:
        print("No tiene cloudflare")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
