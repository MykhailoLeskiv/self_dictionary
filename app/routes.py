from flask_login import current_user, login_user, logout_user, login_required

from app import app, db, api
from flask import render_template, flash, redirect, url_for, request, Blueprint
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.resources import DictionaryApi, UserApi, ChapterApi


@app.route('/')
@login_required
def test():
    return """<h1>Czeszc!</h1>"""


@app.route('/homepage')
def homepage():
    dicts = ['english', 'french']
    return render_template('homepage.html', title=current_user.username, user=current_user, dicts=dicts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


api.add_resource(DictionaryApi, '/users/<int:user_id>/dictionaries')
#api.add_resource(UserApi, '/users/<int:user_id>')
api.add_resource(UserApi, '/users')
api.add_resource(ChapterApi,'/users/<int:user_id>/dictionaries/<int:dictionary_id>/chapters')

api.init_app(app)
