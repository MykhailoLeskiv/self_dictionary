from flask_login import UserMixin
from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Dictionary(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    native_lang = db.Column(db.String(32), index=True, nullable=False)
    foreign_lang = db.Column(db.String(32), index=True, nullable=False)

    def __repr__(self):
        return '<{} - {} dictionary>'.format(self.native_lang, self.foreign_lang)


class Chapter(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    dictionary = db.Column(db.Integer,  db.ForeignKey('dictionary.id'), nullable=False)
    created_datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    chapter_name = db.Column(db.String(32), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Chapter name is {}>'.format(self.chapter_name)


class Word(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.Integer,  db.ForeignKey('chapter.id'), nullable=False)
    word = db.Column(db.String(64), nullable=False)
    translation = db.Column(db.String(64), nullable=False)
    created_datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<{} - {}>'.format(self.word,self.translation)
