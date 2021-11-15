import flask
from flask import render_template, Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://mongo:27017/db")
db = mongodb_client.db

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/month")
def month():
    pass

@app.route("/name", methods=['POST', 'GET'])
def name():
    db.db.insert_one({'name':'yoav', 'age':'30'})
    return flask.jsonify(message='success')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)