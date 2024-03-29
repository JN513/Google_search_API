# Google_search_API

API desenvolvida em Flask com o Intuito de realizar buscas no google e retornar as URLs em formato Json.

## Rotas

A API contem as seguintes rotas:

| URL | Métodos | Descrição | Parâmentros |
| -------- | ------------- | --------- | -------------|
| `/api/search_video` | GET | Pesquisa videos no google com base no queryset passado e retorna as URLs dos mesmos | q: str, lang: str, qtd: int |
| `/api/search_all` | GET | Pesquisa no google com base no queryset passado e retorna as URLs dos resultados | q: str, lang: str, qtd: int  |
| `/api/get_news` | GET | Pesquisa as ultimas noticias no Google News | qtd: int |
| `/api/translate` | GET, POST | Traduz um texto de uma linguagem para outra | lang: str, source: str |
| `/api/get_languages` | GET | Retorna todas as linguagens suportadas | Null |
| `/api/get_lang_codes` | GET | Retorna o codigo de todas as linguagens suportadas | Null |
| `/api/get_finances` | GET | Retorna o valor da cotação | f: str, t: str, r: int |
| `/api/` | GET | Redireciona para o repositorio da API no Github | Null |

como parâmetros é possivel utilizar:

| Parâmetro | Tipo de valor | Default | Obrigatório | Descrição |
| -------- | ------------- | ---------- | --------- | --------- |
| q | str | null | Sim | Termo utilizado na pesquisa |
| lang | str | pt | Não | Linguagem da pesquisa, só funciona nas rotas *search_all* e*search_video* |
| max_results | int  | 30 | Não | Limite de resultados |
| to_iframe | bool | false/0 | Não | Converte o link do youtube para um link pronto para ser usado em um iframe, só funciona na rota *search_video*. |
| source | str | en | Não | Linguagem original do texto que sera traduzido, só funciona na rota *translate*. |
| lang | str | pt | Não | Linguagem para qual o texto sera traduzido, só funciona na rota *translate*. |
| f | str | USD | Não | Moeda base da conversão, só funciona na rota *get_finances* |
| t | str | BRL | Não | Moeda para qual sera realizado a conversão, só funciona na rota *get_finances* |
| r | int | 2 | Não | Quantidade de casas após a virgula, só funcionana rota *get_finances* |


## Dependencias

Para utilizar a API sera necessario ter o Python instalado e as seguintes Bibliotecas:

- Flask
- Google
- googletrans
- bs4
- flask_cors
- requests

## Como instalar

Para instalar as bibliotecas utilize:
``` pip install -r requirements.txt ```

Recomendo que instale as dependencias e utilize a aplicação em uma virtualenv.

Para criar uma virtualenv utilize:
``` python -m venv env ```

Para ativar no Linux utilize:
``` source env/bin/activate ```

Para ativar no Windows utilize:
``` \env\Bin\activate.bat ```

Para desativar tanto no Linux quanto no Windows utilize:
``` deactivate ```

Nota: se você instalar em uma virtualenv toda vez que for utilizar a API sera necessario ativala.

## Execução

Para rodar a API localmente sera necessario exportar a variavel de ambiente "ENV" como "development".

Para exportar no Linux utilize:
``` export ENV=development ```

Para exportar no Windows utilize:
``` set ENV=development ```

Depois disso utilize:
``` python gvsearch.py ```

e a API ira rodar. Caso não queira exportar variaveis de ambiente, utilize:
``` gunicorn gvsearch:app ```

## Exemplos de requisições

<https://google-search-api-oficial.herokuapp.com/api/search_video?q=ola>

<https://google-search-api-oficial.herokuapp.com/api/search_video?q=ola&to_iframe=true>

<https://google-search-api-oficial.herokuapp.com/api/search_video?q=python&lang=en?>

<https://google-search-api-oficial.herokuapp.com/api/search_video?q=java&lang=en&max_results=200>

<https://google-search-api-oficial.herokuapp.com/api/get_news>

<https://google-search-api-oficial.herokuapp.com/api/translate?source=en&lang=pt>

<https://google-search-api-oficial.herokuapp.com/api/get_finances/?f=USD&t=BRL>

## Problemas e sugestões

Fique a vontade para dar sua sujestão ou relatar algum problema na sessão Issues do Git-Hub, caso queira contribuir fique a vontade para criar uma nova branch e realizar um Pull-Request.
