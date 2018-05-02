''' 
    Installation Process 
    sudo pip install flask-login
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Import flask_login 
# LoginManager for Initialize the flask_login
from flask_login import LoginManager , UserMixin ,login_user , login_required , logout_user,current_user

# Initialize the Application
app = Flask(__name__)

# Define the Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////work/python/flask/flask-login-01/database.db'
app.config['SECRET_KEY'] = 'Thisisasecretkey'

# Initialize the Database
db = SQLAlchemy(app)

'''
    Now to Create the dataabsaelogout_user()
    $ python
    >>> from app import db
    >>> db.create_all()

    After Creation of the database check the tables
    check tables 
    .tables
    mysql desc similar command in sqlite
    PRAGMA table_info([User]);

    To Create a user in the database 
    $ python
    >>> from app import db , User
    >>> ironman = User(username='ironman')
    >>> db.session.add(ironman)
    >>> db.session.commit()
    >>> results = User.query.all()
    >>> results[0].username
'''

# Initialize the Flask Login 
login_manager = LoginManager()
login_manager.init_app(app)

# Create The User Database Class 
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    # This will return the User Object for the User_id

@app.route('/')
def index():
    user = User.query.filter_by(username='ironman').first()
    login_user(user)
    return 'Logged in'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged Out'

@app.route('/home')
@login_required
def home():
    return 'Current User is ' +current_user.username
if __name__ == '__main__':
    app.run(debug=True)