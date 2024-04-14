from flask import Flask

from testing import test

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/yaya/<a>/<w>/<h>/<d>/<hr>/<bt>/<g>")
def processer(a, w, h, d, hr, bt, g):
    val = test(int(a), int(w), int(h), int(d), int(hr), int(bt), g)
    return str(val)


# app.run(debug=False, port=9776)
