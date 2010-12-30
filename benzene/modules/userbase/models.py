# -*- coding: utf-8 -*-

from werkzeug import generate_password_hash, check_password_hash
from benzene import db

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def check_password(self, plaintext):
        return check_password_hash(self.password, plaintext)

    def set_password(self, plaintext):
        self.password = generate_password_hash(plaintext)