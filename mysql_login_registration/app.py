from flask import Flask , render_template 
from flask import flash
from flask import redirect , url_for 
from flask import request 
from flask import session , logging
from flask_mysqldb import MySQL 
from wtforms import Form , StringField , TextAreaField,PasswordField, validators
from passlib.hash import sha256_crypt
from data import Articles

app = Flask(__name__)

# MySQL Database Configurations 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'node'
app.config['MYSQL_DB'] = 'user'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MySQL 
mysql = MySQL(app)

# Accesing the article values from data.py

Articles = Articles()
# Landing Page
@app.route('/')
def index():
	return render_template('home.html')

# About Page
@app.route('/about')
def about():
	return render_template('about.html')
 
@app.route('/article')
def articles():
    return render_template('articles.html',articles=Articles)
    
@app.route('/articles/<string:id>')
def article(id):
    return render_template('article.html',id=id)
    
    
# Registration Form Class
    
class RegisterForm(Form):
    name        = StringField('Name',[validators.Length(min=1,max=50)])
    username    = StringField('Username',[validators.Length(min=5,max=20)])
    email       = StringField('E-mail',[validators.Length(min=6,max=40)])
    password    = PasswordField('Password',[validators.DataRequired(),validators.EqualTo('confirm',message='Password didn\'t match')])
    confirm     = PasswordField('Connfirm Password')
    

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    
    if request.method == 'POST' and form.validate():
        name        = form.name.data
        username    = form.username.data
        email       = form.email.data
        password    = sha256_crypt.encrypt(str(form.password.data))
        
        
        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO users(name,email,username,password) VALUES (%s, %s, %s, %s)",(name,email,username,password))
        
        mysql.connection.commit()
        
        cur.close()
        
        flash('You are registered','success')
        
        return redirect(url_for('index'))
    return render_template('register.html',form=form)

# Run the Server and Code
if __name__ == '__main__':
     app.secret_key = '1234#4dasd123!23das#$$'
     app.run(debug=True)
