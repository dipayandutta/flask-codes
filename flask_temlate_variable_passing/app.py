from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def welcome():
	names = ["Ellie","Amanda","Tom"]
	random_name = "James"
	sample_dict = {'x':200,'y':200}
	return render_template('index.html',names=names,name=random_name,dict_show=sample_dict)

if __name__ == '__main__':
	app.run(debug=True)
