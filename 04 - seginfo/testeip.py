'''modulo para discovey de IPs'''
import ipaddress

ip = '192.168.0.1'
saltos = 56487
endereco = ipaddress.ip_address(ip) + saltos
print(ip, f'+ {saltos} => ', endereco)

ip = f'{endereco}/28'
rede = ipaddress.ip_network(ip, strict=False)
print(f'o ip {ip} está na rede: {rede}')
for ip in rede:
    print(ip)
