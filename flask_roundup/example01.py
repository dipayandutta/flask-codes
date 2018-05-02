# -*_ coding: UTF-8 -*-
'''
	example01.py - First Python Flask web applicatiom
'''

from flask import Flask # From 'flask' module import 'Flask' class
app = Flask(__name__)   # Construct an instance of Flask class for the web application

@ app.route('/')   		# Define the home root

def main():
	return "Hello World!"


if __name__ == '__main__':
	app.run() 			# Launch built-in web server and run the flask web application