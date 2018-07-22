# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from flask import Flask
from flask_login import LoginManager
from app.models.base import db


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = 'Please login or register first.'
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
