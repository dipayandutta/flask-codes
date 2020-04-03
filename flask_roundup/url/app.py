from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
	return "This is the Home Page"

@app.route('/hello')
def hello():
	return 'Hello World'

app.route('/hello/<username>')
def hello_username(username):
	return 'Hello {}'.format(username)


if __name__ == '__main__':
	app.run(debug=True)
