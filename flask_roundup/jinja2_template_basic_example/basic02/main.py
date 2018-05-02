from flask import Flask 
from flask import render_template

app = Flask (__name__)

@app.route('/')
def home():
	var_list = [1,2,3,'abc',1.3]
	return render_template('showlist.html',lst = var_list)

if __name__ == '__main__':
	app.run(debug=True)