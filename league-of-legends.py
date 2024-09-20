from flask import Flask, jsonify

app = Flask(__name__)

champions_json = [
    {"name": "Jinx"},
    {"name": "Garen"}
]


@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/champions")
def champions():
    return champions_json
