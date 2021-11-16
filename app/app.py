import flask
from flask import render_template, Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://root:password@mongo:27017/db?authSource=admin")

db = mongodb_client.db

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        month = request.form['month']
    return render_template('index.html')

@app.route("/month", methods=['GET'])
def month():
    if request.method == 'GET':
        name = request.form['name']
        month = request.form['month']
    res = db.db.find()
    return flask.jsonify([month for month in res])

@app.route("/name", methods=['POST', 'GET'])
def name():
    db.db.insert_one({'name':'yoav', 'age':'30'})
    return flask.jsonify(message='success')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    