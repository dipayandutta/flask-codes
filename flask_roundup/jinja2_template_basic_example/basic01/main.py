from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
	variable = 10
	return render_template('showvar.html',var=variable)

if __name__ == '__main__':
	app.run(debug=True)
