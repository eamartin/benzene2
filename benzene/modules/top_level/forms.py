# -*- coding: utf-8 -*-

'''Top level forms for benzene'''

from flaskext.wtf import Form, TextField, validators

class RegistrationForm(Form):
    username = TextField('Username: ')
    email = TextField('Email: ', [validators.Email])
    email_again = TextField('Email again: ', [validators.Email])
    password = TextField('Password: ')
    password_again = TextField('Password again: ')