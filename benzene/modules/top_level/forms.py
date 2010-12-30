# -*- coding: utf-8 -*-

from flaskext.wtf import Form, PasswordField, TextField, ValidationError, \
                         validators
from models import User

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')

    def validate_password(form, field):
        user = User.get(form.username.data)
        if not user:
            raise ValidatonError('No user exists with this username')
        elif not user.check_password(form.password.data):
            raise ValidatonError('Incorrect password')

class RegistrationForm(Form):

