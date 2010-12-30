# -*- coding: utf-8 -*-

from werkzeug import generate_password_hash, check_password_hash
from benzene import db

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def check_password(self, plaintext):
        return check_password_hash(self.password, plaintext)

    def set_password(self, plaintext):
        self.password = generate_password_hash(plaintext)

class UnconfirmedUser(db.Model):
    __tablename__ = 'unconfirmed_users'
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    key = db.Column(db.String(32), primary_key=True)