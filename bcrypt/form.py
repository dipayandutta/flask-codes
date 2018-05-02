from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField
from wtforms.validators import InputRequired , Length

class LoginForm(FlaskForm):
	username = StringField('User Name:', validators=[InputRequired(),Length(max=20)])
	password = PasswordField('Password:', validators=[InputRequired(),Length(min=4,max=20)])
