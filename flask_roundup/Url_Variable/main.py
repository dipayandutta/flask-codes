# -*- coding: UTF-8 -*-

'''
	Variable passing through URL
'''

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home():
	return "Home Page"

	
@app.route('/hello')
def hello():
	return 'Hello, world!'

@app.route('/hello/<username>')
def hello_username(username):
	return 'Hello {}'.format(username)

@app.route('/hello/<int:userid>')
def hello_userid(userid):
	return 'Hello, your ID is : {:d}'.format(userid)

if __name__ == '__main__':
	app.run(debug=True)