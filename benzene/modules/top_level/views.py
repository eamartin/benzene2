# -*- coding: utf-8 -*-

#Top level views for benzene

from flask import render_template

from benzene.modules.top_level import top_level as top

@top.route('/')
def home():
    return render_template('top_level/visitor_home.html')

@top.route('/register')
def register():
    return 'This will be registration page'

@top.route('/login')
def login():
    return 'This will be login page'