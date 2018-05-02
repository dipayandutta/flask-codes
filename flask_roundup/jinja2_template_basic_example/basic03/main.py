# -*- Coding: UTF-8 -*-
'''
	How to get a Form Value using jinja template
'''

from flask import Flask 
from flask import render_template 
from flask import request 

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('form.html')

@app.route('/process',methods=['POST'])
def process():
	username = request.form.get('username')

	if username:
		return render_template('display_username.html',username=username)
	else:
		return 'Please Enter Username'

if __name__ == '__main__':
	app.run(debug=True)