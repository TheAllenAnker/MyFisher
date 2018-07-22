# Author: Allen Anker
# Created by Allen Anker on 22/07/2018
from sqlalchemy import Column, String, Integer, Boolean, Float
from app.models.base import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(32), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone_number = Column(String(12), unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_count = Column(Integer, default=0)
    receive_count = Column(Integer, default=0)

    _password = Column('password', String(100), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)
