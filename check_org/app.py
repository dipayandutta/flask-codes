from flask import Flask 

app = Flask(__name__,template_folder='templates')



# import all views
from view.views import * 

if __name__ == '__main__':
    
    app.run()