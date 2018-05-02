from flask import Flask, render_template, redirect , abort , flash, url_for
from flask_login import LoginManager , login_user , logout_user , current_user , login_required
from models import db,User,load_db,bcrypt
from form import LoginForm

#Flask Setup
app = Flask(__name__)

# Setup the Secret Key
app.config['SECRET_KEY'] = 'asdaijda123142#$!@dae12@#'

# Flask Bcrypt Setup
bcrypt.init_app(app)

# flask SQLAlchemy Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:node@localhost:3306/python_connection'
db.init_app(app) # Bind SQLAlchemy to the Flask Application

# Create a database table and Records
with app.test_request_context():
	load_db(db)

# Flask-Login 
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(username):
	return User.query.get(username)

# Flask - Routes
@app.route('/')
def index():
	return "Hello World!"

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		
		# Query 'user' table with username , Get first row only
		user = User.query.filter_by(username=username).first()

		# Check if username is present 
		if user is None:
			flash('Username or Password is incorrect')
			return redirect(url_for('login'))

		# Check if user is active
		if not user.active:
			flash("Your account is inactive")
			return redirect(url_for(login))

		# Verify the password for the active user
		if not user.verify_password(password):
			flash('Username or Password Incorrect')
			return redirect(url_for('login'))

		# Flask login :- Establish session for this user
		login_user(user)
		return redirect(url_for('startapp'))

	return render_template('login.html',form=form)

@app.route('/startapp')
@login_required
def startapp():
	return render_template('startapp.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.config['SQLALCHEMY_ECHO'] = True
	app.debig = True
	app.run()

