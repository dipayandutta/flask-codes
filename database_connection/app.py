from flask import Flask , render_template
from flask import request
from flask import redirect
import yaml
from flask_mysqldb import MySQL


application = Flask(__name__)

# Database configuration Details
db = yaml.load(open('db.yaml'))
application.config['MYSQL_HOST'] = db['mysql_host']
application.config['MYSQL_USER'] = db['mysql_user']
application.config['MYSQL_PASSWORD'] = db['mysql_password']
application.config['MYSQL_DB'] = db['mysql_db']

# create a MySQL Object
mysql = MySQL(application)

@application.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		userDetails = request.form
		name = userDetails['name']
		email= userDetails['email']

		print (name)
		print (email)

		#Create a MySQL cursor
		cur = mysql.connection.cursor()
		# INSERT the data in the database table
		cur.execute("INSERT INTO user(name,email) VALUES (%s,%s)",(name,email))
		mysql.connection.commit()
		cur.close()
		return redirect('/users')
		#return 'success!'
	
	return render_template('index.html')
@application.route('/users')
def users():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM user")
	if resultValue > 0:
		userDetails = cur.fetchall()
		return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
	application.run(debug=True)
