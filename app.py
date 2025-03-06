from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test1():
    return render_template("t.html")


if __name__ == "__main__":
    app.run()
