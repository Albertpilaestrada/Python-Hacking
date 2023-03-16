import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("127.0.0.1")
print(results)