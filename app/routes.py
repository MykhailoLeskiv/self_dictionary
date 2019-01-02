from app import app
from flask import render_template

@app.route('/')
def test():
    return """<h1>Czeszc!</h1>"""


@app.route('/homepage/')
def homepage():
    user = {'username': 'Petro'}
    dicts = ['english', 'french']
    return render_template('homepage.html', title=user.get('username'), user=user, dicts=dicts)
