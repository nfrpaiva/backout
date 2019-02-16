import requests
import base64
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'Backout'

response = requests.get('https://jsonplaceholder.typicode.com/users')
cabecalho = ['id', 'nome', 'email', 'telefone']
if response.status_code == 200:
    list = response.json()
    with open('arquivo.csv', 'w+') as file:
        file.write(';'.join(cabecalho) + '\n')
        for i in list:
            linha = ';'.join(
                (str(i['id']), i['name'], i['email'], i['phone'])) + '\n'
            file.write(linha)
