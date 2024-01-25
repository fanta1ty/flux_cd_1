from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello FluxCD - v1.0.0.1"
