import requests
import json


apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjI5NDY3MDExNywiYWFpIjoxMSwidWlkIjo1MTUxMjk0MCwiaWFkIjoiMjAyMy0xMS0wN1QyMDozNDoyMi43NTdaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTk3MTc0NTUsInJnbiI6InVzZTEifQ.UN7prxul5z0fl8CAeYJJOCIicrpzK444wm5QrcuKzZM'

apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}

query_nome_quadros = '{ boards (limit:5) {name id} }'
data = {'query': query_nome_quadros}

r_nome_quadros = requests.post(
    url=apiUrl, json=data, headers=headers)  # make request

print(r_nome_quadros.json())

# query para pegar o conteudo de 1 quadro
query2 = '{boards(limit:1) { name id description items { name column_values{title id type text } } } }'
data = {'query': query2}

r = requests.post(url=apiUrl, json=data, headers=headers)  # make request

with open('output.json', "w", encoding='utf-8-sig') as file:
    file.write(r.text)

# query para inserir o conteudo em 1 quadro

query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:5470593200, item_name:$myItemName, column_values:$columnVals) { id } }'
vars = {
    'myItemName': 'Guilherme Rodrigues Santana',
    'columnVals': json.dumps({
        'text0': 'Dev',
        'text': 'Zello',
        "status": 'Parceiro',
        "status5": 'Alta',
        "phone": '551145896325',
        'date' : '2023-08-27'
    })
}

data = {'query': query5, 'variables': vars}
r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
# print(r.json())
