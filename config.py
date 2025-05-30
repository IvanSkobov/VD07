import os

class Config:
    SECRET_KEY = 'твой_секретный_ключ'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

