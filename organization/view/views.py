from application import app
from models.models import Member
from form import LoginForm
from flask import render_template

@app.route('/')
def index():
	firstname = Member.query.first()
	return 'This is First Member'+firstname.name

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('index.html',form=form)
