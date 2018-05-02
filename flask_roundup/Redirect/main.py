# -*- coding: UTF-8 -*-
'''
	Use of function redirect and url_for()
'''

from flask import Flask 
from flask import redirect
from flask import url_for


app = Flask(__name__)

@app.route('/')
def main():
	return redirect(url_for('hello',username='Peter'))

@app.route('/hello/<username>')
def hello(username):
	return 'Hello {}'.format(username)


if __name__ == '__main__':
	app.run(debug=True)