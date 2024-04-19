from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/')
def main():
    return {'Route': '/api/hello'}, {'Route': '/api/restaurantes/'}, {'Route': '/api/restaurantes/?restaurante=query'}

@app.get('/api/hello') #! rota para ser acessada (url)
def hello():
    '''
    Endpoint que exibe uma mensagem incrivel do mundo da programacao!
    '''
    return {'hello world!'}

@app.get('/api/restaurantes/')
def get_restaurante(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #! endpoint/dados
    response = requests.get(url) #! pega os dados da url por meio do get

    if response.status_code == 200: #! verifica se o code é 200(ok)
        dados_json = response.json() #! cria uma variavel para armazenar os dados, response.json() -> retorna os valores da API como JSON
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurante = [] #! cria um dicionario vazio
        for item in dados_json: #! itera sobre a resposta em JSON que recebemos da API
            if item['Company'] == restaurante:
                dados_restaurante.append({ #! adiciona o restante da informacao dos itens *** sempre passando como dicionario ***
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
            })
        return {'Restaurante' : restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}