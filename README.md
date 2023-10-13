# README.md

Este projeto é uma API RESTful criada usando FastAPI, uma biblioteca Python moderna e rápida para construir APIs. A API consulta um banco de dados SQLite para obter informações sobre os intervalos de tempo entre os prêmios ganhos por produtores específicos.

## Instalação

Para executar este projeto, você precisará instalar o FastAPI e o Uvicorn. Você pode fazer isso usando o seguinte comando:


​
pip install -r requirements.txt
​


## Execução

Para executar a API, você pode usar o seguinte comando:


​
uvicorn main:app --reload
​


Isso iniciará o servidor de desenvolvimento Uvicorn na porta 8000. Você pode acessar a documentação da API em http://localhost:8000/docs.

## Rotas

A API possui três rotas:

1. `/producer_max_interval`: Retorna o produtor com o maior intervalo de tempo entre os prêmios.
2. `/producer_min_interval`: Retorna o produtor com o menor intervalo de tempo entre os prêmios.
3. `/awards_interval`: Retorna o produtor com o maior e o menor intervalo de tempo entre os prêmios.

## Exemplo de uso

Você pode usar a biblioteca `requests` para fazer chamadas à API. Aqui está um exemplo de como fazer isso:


​
import requests
​
response = requests.get('http://localhost:8000/producer_max_interval')
print(response.json())
​


Isso retornará um JSON contendo informações sobre o produtor com o maior intervalo de tempo entre os prêmios.

# Docker
docker build -t myimage .

docker run -d --name mycontainer -p 80:80 myimage

## Rotas Docker

1. `http://localhost/producer_max_interval`: Retorna o produtor com o maior intervalo de tempo entre os prêmios.
2. `http://localhost/producer_min_interval`: Retorna o produtor com o menor intervalo de tempo entre os prêmios.
3. `http://localhost/awards_interval`: Retorna o produtor com o maior e o menor intervalo de tempo entre os prêmios.


