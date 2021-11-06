from flask import Flask, json, request, jsonify, redirect
from googlesearch import search
from bs4 import BeautifulSoup
from googletrans import Translator, LANGUAGES, LANGCODES
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)


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
    to_iframe = (
        bool(request.args.get("to_iframe")) if request.args.get("to_iframe") else False
    )

    results = [
        c
        for c in search(f"'{payload}' youtube", stop=qtd if qtd > 30 else 30, lang=lang)
        if "watch?v=" in c or "youtu.be/" in c
    ]

    if to_iframe:
        for i in range(len(results)):
            if "watch?v=" in results[i]:
                results[i] = results[i].replace("watch?v=", "embed/")
            elif "youtu.be/" in results[i]:
                results[i] = results[i].replace("youtu.be/", "www.youtube.com/embed/")

    return jsonify({"sucess": True, "links": results[:qtd]})


@app.route("/get_news", methods=["GET"])
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


@app.route("/translate", methods=["GET", "POST"])
def translate():
    payload = request.args.get("q") or request.form.get("q")

    if not payload:
        return jsonify({"sucess": False, "error": "Queryset nao fornecido"})

    lang = request.args.get("lang") if request.args.get("lang") else "pt"
    source = request.args.get("source") if request.args.get("source") else "en"

    if LANGCODES.get(lang):
        return jsonify({"sucess": False, "error": "Idioma de saida nao suportado"})

    if LANGCODES.get(source):
        return jsonify({"sucess": False, "error": "Idioma de entrada nao suportado"})

    translator = Translator()
    translation = translator.translate(payload, dest=lang, src=source)

    return jsonify({"sucess": True, "translation": translation.text})


@app.route("/get_languages", methods=["GET"])
def get_languages():
    return jsonify({"sucess": True, "languages": LANGUAGES})


@app.route("/get_lang_codes", methods=["GET"])
def get_lang_codes():
    return jsonify({"sucess": True, "lang_codes": LANGCODES})


@app.route("/get_finances/", methods=["GET"])
def cotacao():
    f = request.args.get("f") if request.args.get("f") else "USD"
    t = request.args.get("t") if request.args.get("t") else "BRL"

    html = requests.get(f"https://www.google.com/finance/quote/{f}-{t}")
    soup = BeautifulSoup(html.text, "html.parser")
    valor = soup.select('[class="YMlKec fxKbKc"]')
    try:
        valor = float(valor[0].text)
        result = jsonify({"sucess": True, "valor": round(valor, 2)})
        return result
    except:
        return {"error": "Ocorreu um erro"}


@app.route("/")
def index():
    return redirect("https://github.com/JN513/Google_search_API")


if os.environ.get("ENV") == "development" and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
