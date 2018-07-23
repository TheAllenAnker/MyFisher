# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from . import web
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import  db
from app.models.user import User


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST'and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            # get the last open page url before this login page
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('Email address does not exist or password does not match.')
    return render_template('auth/login.html', form=form)


@web.route('/reset/forget_password', methods=['GET', 'POST'])
def forget_password_request():
    return render_template('auth/forget_password_request.html')