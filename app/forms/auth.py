# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    nickname = StringField(validators=[DataRequired(message='Nickname cannot be empty'),
                                       Length(8, 16, message='Nickname length must between 8 and 16 characters')])
    email = StringField(validators=[DataRequired(message='Email address is required'), Length(8, 64),
                                    Email(message='Email format is not correct')])
    password = PasswordField(validators=[DataRequired(message='Password is required'), Length(8, 32)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email address has been registered.')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Nickname is taken, please choose another one.')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(message='Email address is required'),
                                    Email(message='Email format is not correct')])
    password = PasswordField(validators=[DataRequired(message='Password is required')])
