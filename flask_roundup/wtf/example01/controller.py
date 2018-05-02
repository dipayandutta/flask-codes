import os 
import binascii
from flask import Flask , render_template
from form import LoginForm 
from flask import redirect 
from flask import url_for
from flask import flash 

app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))

@app.route('/',methods=['POST'])
def main():
	form = LoginForm()

	if form.validate_on_submit():

		username = request.form.get('username')
		password = request.form.get('password')
		print username
		print password

		if (form.username.data == 'Peter' and form.password.data == 'parker'):
			return redirect(url_for('success'))
		else:
			flash('Wrong Username or Password')

	return render_template('login.html',form = form)

@app.route('/success')
def success():
	return 'Username and password matched !'

if __name__ == '__main__':
	app.run(debug=True)
