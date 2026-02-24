from flask import Flask,render_template, request
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/coinFlip")
def coinFlip():
    return render_template("coin.html")

@app.route("/coinData")
def coinData():
    rnd=random.randint(0,1)
    return ["TAILS", "HEADS"][rnd]


app.run(debug=True)
