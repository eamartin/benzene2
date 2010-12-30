# -*- coding: utf-8 -*-

#Top level views for benzene

from flask import redirect, render_template, request, session, url_for

from benzene import app, db

from forms import LoginForm
from models import User

@app.route('/')
def home():
    '''Should be static or at least cached'''
    return render_template('top_level/visitor_home.html')

@app.route('/register')
def register():
    return 'This will be registration page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        session['user'] = form.username.data
        return redirect(url_for('home'))
    return render_template('top_level/login.html', form=LoginForm())

@app.route('/logout')
def logout():
    if 'user' in session:
        del session['user']
    return redirect('home')