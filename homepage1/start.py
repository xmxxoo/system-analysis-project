from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('html', "index.html")

@app.route("/<path:name>")
def start(name):
    return send_from_directory("html", name)