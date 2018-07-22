# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from . import web
from flask import render_template


@web.route('/')
def index():
    return render_template('index.html')