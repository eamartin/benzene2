# -*- coding: utf-8 -*-

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

from benzene.modules import top_level, userbase

app = Flask(__name__)

app.config.from_object('benzene.default_settings')
try:
    app.config.from_envvar('BENZENE_SETTINGS')
except RuntimeError:
    pass

db = SQLAlchemy(app)

import error_handlers
app.register_module(top_level.top_level)
app.register_module(userbase.userbase, url_prefix='/userbase')

