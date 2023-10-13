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


# Testes unitários para a API
Este arquivo contém os testes unitários para a API.
## Testes
### Teste 1: Obter o intervalo máximo do produtor
Este teste verifica se a API retorna o intervalo máximo do produtor.

​
python
def test_get_producer_max_interval(self):
    response = self.client.get("/producer_max_interval")
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertIn("max", data)

### Teste 2: Obter o intervalo mínimo do produtor
Este teste verifica se a API retorna o intervalo mínimo do produtor.

​
python
def test_get_producer_min_interval(self):
    response = self.client.get("/producer_min_interval")
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertIn("min", data)

### Teste 3: Obter o intervalo de prêmios
Este teste verifica se a API retorna o intervalo de prêmios.

​
python
def test_get_awards_interval(self):
    response = self.client.get("/awards_interval")
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertIn("min", data)
    self.assertIn("max", data)

## Executando os testes
Para executar os testes, basta executar o seguinte comando:
​

unittest.main()