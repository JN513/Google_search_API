from flask import Flask, request, jsonify, redirect
from googlesearch import search
from bs4 import BeautifulSoup
import os
import requests

app = Flask(__name__)


@app.route("/search_all", methods=["GET"])
def get_all():
    payload = request.args.get("q")

    if not payload:
        return jsonify({"sucess": False, "error": "Queryset nao fornecido"})

    lang = request.args.get("lang") if request.args.get("lang") else "pt"
    qtd = (
        int(request.args.get("max_results")) if request.args.get("max_results") else 30
    )

    qtd = qtd if qtd <= 100 else 100

    results = [c for c in search(f"{payload}", stop=qtd, lang=lang)]

    return jsonify({"sucess": True, "links": results})


@app.route("/search_video", methods=["GET"])
def get_videos():
    payload = request.args.get("q")

    if not payload:
        return jsonify({"sucess": False, "error": "Queryset nao fornecido"})

    lang = request.args.get("lang") if request.args.get("lang") else "pt"
    qtd = (
        int(request.args.get("max_results")) if request.args.get("max_results") else 30
    )

    qtd = qtd if qtd <= 100 else 100

    results = [
        c
        for c in search(f"'{payload}' youtube", stop=qtd if qtd > 30 else 30, lang=lang)
        if "watch?v=" in c
    ]

    return jsonify({"sucess": True, "links": results[:qtd]})


@app.route("/search_news", methods=["GET"])
def get_news():
    site = requests.get("https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419")
    noticias = BeautifulSoup(site.text, "html.parser")

    qtd = int(request.args.get("max_results")) if request.args.get("max_results") else 5

    news = list()

    for item in noticias.findAll("item")[:qtd]:
        dados = {
            "title": item.title.text,
            "description": BeautifulSoup(item.description.text, "lxml").text,
            "pub_date": item.pubdate.text,
        }

        news.append(dados)

    return jsonify({"sucess": True, "news": news})


@app.route("/")
def index():
    return redirect("https://github.com/JN513/Google_search_API")


if os.environ.get("ENV") == "development" and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
