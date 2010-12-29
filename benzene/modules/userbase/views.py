# -*- coding: utf-8 -*-

from benzene.modules.userbase import userbase

@userbase.route('/')
def index():
    return 'USERBASE!'