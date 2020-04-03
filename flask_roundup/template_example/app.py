from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route('/')
def main():
	return render_template('hello.html')

if __name__ == '__main__':
	application.run()
