from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Khush'}
    posts = [
        {
            'author': {'username':'Shlok'},
            'body': 'Going on a hot date!'
        },
        {
            'author': {'username': 'Hitesh'},
            'body': 'Making soup for dinner.'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)
