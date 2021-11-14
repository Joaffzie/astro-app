from flask import Flask, Response, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/month")
def month():
    pass