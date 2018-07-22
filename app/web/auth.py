# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from . import web
from flask import render_template, request, url_for, redirect
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import  db
from app.models.user import User


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST'and form.validate():
        with db.auto_commit():
            user = User()
            # user.nickname = form.nickname.data
            # user.email = form.email.data
            # user.password = form.password.data
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():

        return render_template('index.html')
    return render_template('auth/login.html', form=form)


@web.route('/reset/forget_password', methods=['GET', 'POST'])
def forget_password_request():
    return render_template('auth/forget_password_request.html')