from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
def test():
    return """<h1>Czeszc!</h1>"""


@app.route('/homepage/')
def homepage():
    user = {'username': 'Petro'}
    dicts = ['english', 'french']
    return render_template('homepage.html', title=user.get('username'), user=user, dicts=dicts)


@app.route('/login', methods=['POST'])
def login():
    form = LoginForm('/login')
    return render_template('login.html', title='Sign in', form=form)
