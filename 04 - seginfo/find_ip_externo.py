'''para capturar informacoes do IP externo'''
import json
from urllib.request import urlopen


url = 'https://ipinfo.io/json'
response = urlopen(url, timeout=600)
dados = json.load(response)

# print(dados)
print(dados['ip'])
print(dados['hostname'])
print(dados['city'])
print(dados['region'])
print(dados['country'])
print(dados['loc'])
print(dados['org'])
print(dados['postal'])
print(dados['timezone'])
print(dados['readme'])
