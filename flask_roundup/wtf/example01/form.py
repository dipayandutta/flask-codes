from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField
from wtforms.validators import InputRequired , Length

class LoginForm(FlaskForm):
	username = StringField('Username: ',validators=[InputRequired(),Length(min=3,max=40)])
	password = PasswordField('Password :',validators=[InputRequired(),Length(min=3,max=40)])

