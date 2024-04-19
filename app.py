import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #! endpoint/dados
response = requests.get(url) #! pega os dados da url por meio do get
print(response)  #! retorna -> 200(OK) -> status code

if response.status_code == 200: #! verifica se o code é 200(ok)
    dados_json = response.json() #! cria uma variavel para armazenar os dados, response.json() -> retorna os valores da API como JSON
    dados_restaurante = {} #! cria um dicionario vazio
    for item in dados_json: #! itera sobre a resposta em JSON que recebemos da API
        nome_do_restaurante = item['Company'] #! cria uma variavel, pegando os valores do atributo *** company *** da API
        if nome_do_restaurante not in dados_restaurante: #! verifica se o valor náo existe no dicionario
            dados_restaurante[nome_do_restaurante] = [] #! cria uma lista vazia com os dados do *** company ***

        dados_restaurante[nome_do_restaurante].append({ #! adiciona o restante da informacao dos itens *** sempre passando como dicionario ***
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'Erro foi {response.status_code}')

print(dados_restaurante['McDonald’s']) #! printa os valores passando por referencia, um * filtro * de qual company quer exibir

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json' #! cria uma variavel que vai ser o nome do arquivo
    with open(nome_do_arquivo, 'w') as arquivo_restaurante: #! funcao do python para criar arquivo with open(nome_do_arquivo, 'w') -> w de WRITE(escrever no arquivo), as define um apelido para funcao
        json.dump(dados, arquivo_restaurante, indent=4) #! json_dump espera 4 parametros, dados, arquivo_restaurante -> que 'e o arquivo ja gerado, indent que serve para identacao.