from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)

# load the main Configuration file
app.config.from_pyfile('/work/python/flask/organization/configuration/config.py')

# make the database instance
db = SQLAlchemy(app)

# import all views 
from view.views import * 

if __name__ == '__main__':
	app.run()

