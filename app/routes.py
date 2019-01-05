from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm

@app.route('/')
def test():
    return """<h1>Czeszc!</h1>"""


@app.route('/homepage/')
def homepage():
    user = {'username': 'Petro'}
    dicts = ['english', 'french']
    return render_template('homepage.html', title=user.get('username'), user=user, dicts=dicts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('homepage'))
    return render_template('login.html', title='Sign in', form=form)
