from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Flask SQLAlchemy Initialization
db = SQLAlchemy()

# Flask-BCrypt Initialization
bcrypt = Bcrypt()

class User(db.Model):
	username = db.Column(db.String(30),primary_key=True)
	pwhash   = db.Column(db.String(300),nullable=False)
	active   = db.Column(db.Boolean,nullable=False,default=False)

	def __init__(self,username,password,active=False):
		self.pwhash 	= bcrypt.generate_password_hash(password)
		self.username = username
		self.active   = active

	# Convert Method to property
	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return self.active

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return self.username

	def verify_password(self,password_in):
		return bcrypt.check_password_hash(self.pwhash,password_in)

def load_db(db):
	db.drop_all()
	db.create_all()
	db.session.add_all([User('IronMan','avengers',True),User('Dr.Strange','xxxx')])
	db.session.commit()

