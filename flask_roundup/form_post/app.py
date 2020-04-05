from flask import Flask
from flask import render_template
from flask import request

application = Flask(__name__)

@application.route('/')
def home():
	return render_template('form.html')

@application.route('/process',methods=['POST'])
def process():
	username = request.form.get('username')

	if username:
		return render_template('display.html',username=username)
	else:
		return 'Please Insert Name'

if __name__ == '__main__':
	application.run(debug=True)
