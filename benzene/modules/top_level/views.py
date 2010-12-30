# -*- coding: utf-8 -*-

#Top level views for benzene

from flask import redirect, render_template, request, session, url_for

from benzene.modules.top_level import top_level as top

from forms import LoginForm
from models import User

@top.route('/')
def home():
    '''Should be static or at least cached'''
    return render_template('top_level/visitor_home.html')

@top.route('/register')
def register():
    return 'This will be registration page'

@top.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        session['user'] = form.username.data
        return redirect(url_for('home'))
    return render_template('top_level/login.html', form=LoginForm())

@top.route('/logout')
def logout():
    if 'user' in session:
        del session['user']
    return redirect('home')