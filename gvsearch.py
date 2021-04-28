from flask import Flask, request, jsonify
from googlesearch import search
import os

app = Flask(__name__)

@app.route("/search_all", methods=["GET"])
def get_all():
    payload = request.args.get("q")

    if payload == None:
        return jsonify({"sucess": False, "error":"Q nao fornecido"})

    results = [c for c in search(f"{payload}", stop=30)]

    return jsonify({"sucess":True, "links":results})

@app.route("/search_video", methods=["GET"])
def get_videos():
    payload = request.args.get("q")

    if payload == None:
        return jsonify({"sucess": False, "error":"Q não fornecido"})

    results = [c for c in search(f"'{payload}' youtube", stop=30) if "watch?v=" in c]

    return jsonify({"sucess":True, "links":results})

if os.environ.get("ENV") == "development":
    if __name__ == '__main__':
        app.run(host = '0.0.0.0')