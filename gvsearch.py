from flask import Flask, request, jsonify
from googlesearch import search
import os

app = Flask(__name__)


@app.route("/search_all", methods=["GET"])
def get_all():
    payload = request.args.get("q")

    if not payload:
        return jsonify({"sucess": False, "error": "Queryset nao fornecido"})

    lang = request.args.get("lang") if request.args.get("q") else "pt"
    qtd = (
        int(request.args.get("max_results")) if request.args.get("max_results") else 30
    )

    results = [c for c in search(f"{payload}", stop=qtd, lang=lang)]

    return jsonify({"sucess": True, "links": results})


@app.route("/search_video", methods=["GET"])
def get_videos():
    payload = request.args.get("q")

    if not payload:
        return jsonify({"sucess": False, "error": "Queryset nao fornecido"})

    lang = request.args.get("lang") if request.args.get("q") else "pt"
    qtd = (
        int(request.args.get("max_results")) if request.args.get("max_results") else 30
    )

    results = [
        c for c in search(f"'{payload}' youtube", stop=30, lang=lang) if "watch?v=" in c
    ]

    return jsonify({"sucess": True, "links": results[:qtd]})


if os.environ.get("ENV") == "development" and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
