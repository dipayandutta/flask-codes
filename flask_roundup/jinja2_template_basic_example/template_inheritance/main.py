from flask import Flask 
from flask import render_template 

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('derived.html')

if __name__ == '__main__':
	app.run(debug=True)
