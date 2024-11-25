from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from testing import test

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
    return jsonify({"success": "ok"})


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/yaya/<a>/<w>/<h>/<d>/<hr>/<bt>/<g>")
def processer(a, w, h, d, hr, bt, g):
    val = test(int(a), int(w), int(h), int(d), int(hr), int(bt), g)
    return str(val)


if __name__ == "__main__":
    app.run(debug=True, port=8001, host="0.0.0.0")
