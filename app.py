from flask import Flask, request, jsonify
from googlesearch import search

app = Flask(__name__)

@app.route("/search_all", methods=["GET"])
def get_all():
    results = []
    payload = request.args.get("q")

    if payload == None:
        return jsonify({"sucess": False, "error":"Q nao fornecido"})

    for c in search(f"{payload}", stop=30):
        results.append(c)

    return jsonify({"sucess":True, "links":results})

@app.route("/search_video", methods=["GET"])
def get_videos():
    results = []
    payload = request.args.get("q")

    if payload == None:
        return jsonify({"sucess": False, "error":"Q não fornecido"})

    for c in search(f"'{payload}' youtube", stop=30):
        if "watch?v=" in c:
            results.append(c)

    return jsonify({"sucess":True, "links":results})

if __name__ == '__main__':
    app.run(host = '0.0.0.0')