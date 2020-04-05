from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dipayan/WORK/python/flask-codes/example.db'
db = SQLAlchemy(app)

class ExampleTable(db.Model):
	id = db.Column(db.Integer,primary_key=True)
