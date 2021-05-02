# Google_search_API

API desenvolvida em Flask com o Intuito de realizar buscas no google e retornar as URLs em formato Json.

## Rotas

A API contem as seguintes rotas:

| URL | Métodos | Descrição |
| -------- | ------------- | --------- |
| `/search_video` | GET | Pesquisa videos no google com base no queryset passado e retorna as URLs dos mesmos |
| `/search_all` | GET | Pesquisa no google com base no queryset passado e retorna as URLs dos resultados |
| `/get_news` | GET | Pesquisa as ultimas noticias no Google News |

como parâmetros é possivel utilizar:

| Parâmetro | Tipo de valor | Default | Obrigatório | Descrição |
| -------- | ------------- | ---------- | --------- | --------- |
| q | str | null | Sim | Termo utilizado na pesquisa |
| lang | str | pt | Não | Linguagem da pesquisa |
| max_results | int  | 30 | Não | Limite de resultados |


## Dependencias

Para utilizar a API sera necessario ter o Python instalado e as seguintes Bibliotecas:

- Flask
- Google

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

<https://gvcapi.herokuapp.com/search_video?q=ola>

<https://gvcapi.herokuapp.com/search_video?q=python&lang=en?>

<https://gvcapi.herokuapp.com/search_video?q=java&lang=en&max_results=200>

## Problemas e sugestões

Fique a vontade para dar sua sujestão ou relatar algum problema na sessão Issues do Git-Hub, caso queira contribuir fique a vontade para criar uma nova branch e realizar um Pull-Request.
