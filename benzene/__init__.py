# -*- coding: utf-8 -*-

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

from benzene.modules.userbase import userbase

app = Flask(__name__)

app.config.from_object('benzene.default_settings')
try:
    app.config.from_envvar('BENZENE_SETTINGS')
except RuntimeError:
    pass

db = SQLAlchemy(app)

import benzene.top_level_views
app.register_module(userbase, url_prefix='/userbase')

