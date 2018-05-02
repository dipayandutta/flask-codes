''' 
    Installation Process 
    sudo pip install flask-login
'''
from urlparse import urlparse, urljoin
from flask import Flask , render_template , request , redirect , session 
from flask_sqlalchemy import SQLAlchemy
# Import flask_login 
# LoginManager for Initialize the flask_login
from flask_login import LoginManager , UserMixin ,login_user , login_required , logout_user,current_user

# Initialize the Application
app = Flask(__name__)

# Define the Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////work/python/flask/flask-login-01/database.db'
app.config['SECRET_KEY'] = 'Thisisasecretkey'
app.config['USE_SESSION_FOR_NEXT'] = True 

# Initialize the Database
db = SQLAlchemy(app)

# Initialize the Flask Login 
login_manager = LoginManager()
login_manager.init_app(app)
# login_view is required when i have initialaised a route but didn't declear it 
login_manager.login_view = 'login' # The login View to stop displaying the Unathorized Page

#Put the login Message 
login_manager.login_message = "Logg in to visit " # This message will be displayed the login.html

# Create The User Database Class 
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    # This will return the User Object for the User_id

# Creating a userlogin Route
@app.route('/login')
def login():
    # Set the session 
    session['next'] = request.args.get('next')
    return render_template('login.html')

# Function to check if the redirection of the URL is inside the domain
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

# The Login Route         
@app.route('/logmein',methods=['POST'])
def logmein():
 
    # Collecting the username from the form
    username = request.form['username']

    #Query the sqlite database using the username
    user = User.query.filter_by(username=username).first()

    #Checking if the user is present in the database or 
    if not user:
        return 'user not found' # If user is not present in the database display this message
    
    # Else login the user use th login_user() method from flask --> flask_login
    login_user(user)

    if 'next' in session:
        next = session['next']
        if is_safe_url(next):
            return redirect(next)

    return "Logged In"

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