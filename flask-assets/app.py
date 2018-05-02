from flask import Flask , render_template
from flask_assets import Bundle , Environment
app = Flask(__name__)

js = Bundle('home.js','add.js',output='gen/main.js')
assets = Environment(app)
assets.register('main_js',js)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)