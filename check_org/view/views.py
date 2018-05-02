from app import app 
from flask import request
from flask import render_template,url_for , session ,logging,redirect
from passlib.hash import sha256_crypt 


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/article')
def articles():
    return render_template('articles.html',articles=Articles)

@app.route('/articles/<string:id>')
def article(id):
    return render_template('article.html',id=id)



